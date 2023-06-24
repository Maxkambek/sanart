from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=123)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Invalid phone number')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        ('Yuridik', 'Yuridik'),
        ('Jismoniy', 'Jismoniy')
    )
    phone = models.CharField(max_length=13, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    role = models.CharField(max_length=123, choices=ROLE, default='Jismoniy')
    is_separate = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone


class UserDetailJismoniy(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_details')
    citizen = models.CharField(max_length=333)
    inn = models.CharField(max_length=123)
    fsl = models.CharField(max_length=333)
    date_birth = models.CharField(max_length=123)
    gender = models.CharField(max_length=123, choices=GENDER)
    passport_num = models.CharField(max_length=123)
    passport_date = models.CharField(max_length=123)
    jshshir = models.CharField(max_length=15)
    passport_given_by = models.CharField(max_length=333)

    def __str__(self):
        return self.user.phone


class UserDetailYuridik(models.Model):
    name = models.CharField(max_length=123)
    inn = models.CharField(max_length=123)
    director = models.CharField(max_length=1234)
    registered_date = models.CharField(max_length=123)
    address = models.CharField(max_length=333)
    mfo = models.CharField(max_length=333)
    bank = models.CharField(max_length=1234)
    account = models.CharField(max_length=1234)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_detail_yuridik')

    def __str__(self):
        return self.user.phone


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = ("Telefon raqamni tasdiqlash")
        verbose_name_plural = ("Telefon raqam tasdiqlash")

    phone = models.CharField(max_length=15, verbose_name="Telefon raqam")
    code = models.CharField(max_length=10, verbose_name="Kod")

    def __str__(self):
        return self.phone


class UserBalance(models.Model):
    amount = models.PositiveBigIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.phone
