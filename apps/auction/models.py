from __future__ import unicode_literals
from django.db import models
from accounts.models import User
from main.models import Property
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.utils import timezone


class Auction(models.Model):
    start = models.DateTimeField(auto_now=False)
    item = models.OneToOneField(
        Property, on_delete=models.CASCADE, related_name="auction")
    cap_time = models.DateTimeField(auto_now=False)


class Message(models.Model):
    auction = models.ForeignKey(
        Auction, on_delete=models.CASCADE, related_name="auction")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.phone + str(self.price)


class CustomerCare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()


#############
# RECEIVERS #
#############


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Property.objects.filter(slug=slug).order_by("id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Property)
def pre_save_item_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    if kwargs.get("created"):
        instance.current_price = instance.start_price


@receiver(pre_save, sender=Message)
def pre_save_current_price_updater(sender, instance, *args, **kwargs):
    item = instance.auction.item
    item.current_price = instance.price
    item.save()
