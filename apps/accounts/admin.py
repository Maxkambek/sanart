from django.contrib import admin
from .models import User, VerifyPhone, Region, District
from .translation import CustomTransAdmin, StackTransAdmin


class DistrictInline(StackTransAdmin):
    model = District
    extra = 0


@admin.register(Region)
class Admin(CustomTransAdmin):
    inlines = [DistrictInline]


admin.site.register(User)
admin.site.register(VerifyPhone)
