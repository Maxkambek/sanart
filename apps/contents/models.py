from django.db import models


class News(models.Model):
    video = models.FileField(upload_to='files/', null=True, blank=True)
    title = models.CharField(max_length=223)
    views = models.PositiveIntegerField()
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone = models.CharField(max_length=123)
    time = models.CharField(max_length=123)
    address = models.CharField(max_length=123)
    email = models.CharField(max_length=123)

    def __str__(self):
        return self.phone


class GetInTouch(models.Model):
    phone = models.CharField(max_length=123)

    def __str__(self):
        return self.phone
