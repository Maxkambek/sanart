from random import randint
from rest_framework import generics, status, permissions, response, views
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .utils import verify
from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, ResetPasswordSerializer, \
    VerifyPhoneSerializer, ResetPasswordConfirmSerializer, UserDetailYuridikSerializer, UserDetailJismoniySerializer, \
    UserSerializer
from .models import User, VerifyPhone, District, Region, UserDetailJismoniy, UserDetailYuridik
from .serializers import RegionSerializer, DistrictSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        if User.objects.filter(phone=phone, is_active=True).first():
            return response.Response({'message': "This number already exist"}, status=status.HTTP_302_FOUND)
        code = str(randint(100000, 1000000))
        ver = VerifyPhone.objects.filter(phone=phone).first()
        if ver:
            ver.delete()
        verify(phone, code)
        VerifyPhone.objects.create(phone=phone, code=code)
        return response.Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                                 status=status.HTTP_200_OK)


class RegisterConfirmAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = VerifyPhoneSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        password = self.request.data['password']
        code = self.request.data['code']
        v = VerifyPhone.objects.filter(phone=phone, code=code).first()
        if v:
            v.delete()
        else:
            return response.Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(
            phone=phone,
            password=password
        )
        user.is_active = True
        user.save()
        token = Token.objects.create(user=user)
        data = {
            'message': 'User verified',
            'token': str(token),
            'user_id': user.id,
            'user': user.role,
            'is_separate': user.is_separate,
        }
        return response.Response(data, status=status.HTTP_201_CREATED)


class LoginAPI(generics.GenericAPIView):
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = request.data['phone']
        user = User.objects.filter(phone=phone).first()
        if not user:
            return response.Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        ver = VerifyPhone.objects.filter(phone=phone).first()
        if ver:
            ver.delete()
        code = str(randint(100000, 1000000))
        verify(phone, code)
        VerifyPhone.objects.create(phone=phone, code=code)
        return response.Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                                 status=status.HTTP_200_OK)


class LoginVerifyAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = VerifyPhoneSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        code = self.request.data['code']
        v = VerifyPhone.objects.filter(phone=phone, code=code).first()
        if v:
            v.delete()
        else:
            return response.Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(phone=phone).first()
        token = Token.objects.get(user=user)
        data = {
            'message': 'User verified',
            'token': str(token),
            'user': user.role,
            'is_separate': user.is_separate,
            'user_id': user.id
        }
        return response.Response(data, status=status.HTTP_201_CREATED)


class ChangePasswordAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    def patch(self, request, *args, **kwargs):
        user = request.user
        pas1 = request.data['password']
        pas2 = request.data['old_password']
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if user.check_password(pas2):
            user.set_password(pas1)
            user.save()
            return response.Response({'success': True, 'message': 'Successfully changed password'})
        return response.Response({'message': 'old password incorrect'}, status=400)


class ResetPasswordAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        code = str(randint(10000, 100000))
        verify(phone, code)
        VerifyPhone.objects.create(phone=phone, code=code)
        return response.Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"})


class VerifyPhoneResetPasswordAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        code = self.request.data['code']
        v = VerifyPhone.objects.filter(phone=phone, code=code).first()
        if v:
            v.delete()
        else:
            return response.Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response({'message': "Successfully verified!"})


class ResetPasswordConfirmAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        phone = serializer.validated_data['phone']
        pas1 = serializer.validated_data['password']
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(phone=phone).first()
        user.set_password(pas1)
        user.save()
        return response.Response({'success': True, 'message': "Password restored"})


class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DistrictListAPIView(generics.ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        queryset = District.objects.all()
        region_id = self.request.GET.get('region_id')
        if region_id:
            queryset = queryset.filter(region_id=region_id)
        return queryset


class UserDetailYurudikCreateAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    serializer_class = UserDetailYuridikSerializer
    queryset = UserDetailYuridik.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class UserDetailJismoniyCreateAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    serializer_class = UserDetailJismoniySerializer
    queryset = UserDetailJismoniy.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class UserDetailYuridikRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    serializer_class = UserDetailYuridikSerializer
    queryset = UserDetailYuridik.objects.all()

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        instance = UserDetailYuridik.objects.filter(user=user).first()
        serializer = self.get_serializer(instance=instance, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = UserDetailYuridik.objects.filter(user=self.request.user).first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = UserDetailYuridik.objects.filter(user=self.request.user).first()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailJismoniyRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    serializer_class = UserDetailJismoniySerializer
    queryset = UserDetailJismoniy.objects.all()

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        instance = UserDetailJismoniy.objects.filter(user=user).first()
        serializer = self.get_serializer(instance=instance, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = UserDetailJismoniy.objects.filter(user=self.request.user).first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = UserDetailJismoniy.objects.filter(user=self.request.user).first()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserChangeRole(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.request.user, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.request.user
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
