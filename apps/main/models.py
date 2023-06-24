from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from uuid import uuid4


class Catalog(models.Model):
    name = models.CharField(max_length=223)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class CatalogVideo(models.Model):
    video = models.FileField(upload_to='files')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='catalog_videos')


class Property(models.Model):
    TRADE_TYPE = (
        ('Auction', 'Action'),
        ('Sale', 'Sale')
    )
    TRADE_STYLE = (
        ('Increase', 'Increase'),
        ('OneTime', 'OneTime')
    )
    STATUS = (
        ('New', 'New'),
        ('Waiting', 'Waiting'),
        ('Send', 'Send'),
        ('Ordered', 'Ordered')
    )
    slug = models.SlugField(blank=True, null=True)
    name = models.CharField(max_length=450)
    sort_number = models.PositiveIntegerField(unique=True)
    views = models.PositiveIntegerField(default=1)
    deadline = models.DateTimeField()
    start_price = models.PositiveIntegerField()
    trade_type = models.CharField(choices=TRADE_TYPE, max_length=100)
    trade_style = models.CharField(choices=TRADE_STYLE, max_length=100)
    start_date = models.DateTimeField()
    back_price = models.CharField(max_length=123)
    first_step_percent = models.PositiveIntegerField(default=10)
    address = models.CharField(max_length=300)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    description = models.TextField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=123)
    video = models.FileField(upload_to='files/', null=True, blank=True)
    current_price = models.IntegerField(default=0.0)

    def __str__(self):
        return self.name

    @property
    def get_first_step_price(self):
        return self.start_price * 0.1

    @property
    def auction_status(self):
        today = timezone.now()
        auction = self.auction
        if auction.cap_time < today:
            return "past"
        elif auction.start > today:
            return "upcoming"
        else:
            return "live"

    def time_to_end(self):
        today = timezone.now()
        auction = self.auction
        if auction.cap_time < today:
            return 0
        else:
            return auction.cap_time - today

    def time_to_start(self):
        today = timezone.now()
        auction = self.auction
        if auction.cap_time < today:
            return 0
        else:
            return today - auction.start


class PropertyImages(models.Model):
    obj = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_images')
    image = models.ImageField(upload_to='images/')


class PropertyDetails(models.Model):
    key = models.CharField(max_length=223, null=True, blank=True)
    value = models.CharField(max_length=223, null=True, blank=True)
    obj = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_details')


class PropertyFiles(models.Model):
    file = models.FileField(upload_to='files/')
    obj = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_files')
