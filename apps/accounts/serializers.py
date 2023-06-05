from rest_framework import serializers
from .models import User, Region, District, UserDetailYuridik, UserDetailJismoniy


class UserDetailYuridikSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetailYuridik
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['role']


class UserDetailJismoniySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetailJismoniy
        exclude = ['user']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'region', 'name']


class VerifyPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)
    code = serializers.IntegerField(max_value=9999)
    password = serializers.CharField(max_length=64, min_length=4, write_only=True)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone']

    phone = serializers.CharField(max_length=12)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'password']

    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12)


class ResetPasswordConfirmSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12)
    password = serializers.CharField(max_length=64)


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'old_password']

    password = serializers.CharField(max_length=64, write_only=True)
    old_password = serializers.CharField(max_length=64, write_only=True)
