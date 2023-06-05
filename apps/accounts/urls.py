from django.urls import path
from .views import LoginAPI, RegisterAPI, RegisterConfirmAPI, ChangePasswordAPI, ResetPasswordAPI, \
    ResetPasswordConfirmAPI, VerifyPhoneResetPasswordAPI, RegionListAPIView, \
    DistrictListAPIView, UserChangeRole, UserDetailRUDAPI

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('register-confirm/', RegisterConfirmAPI.as_view()),
    path('change-password/', ChangePasswordAPI.as_view()),
    path('reset-password/', ResetPasswordAPI.as_view()),
    path('verify-reset-password/', VerifyPhoneResetPasswordAPI.as_view()),
    path('confirm-reset-password/', ResetPasswordConfirmAPI.as_view()),
    path('regions/', RegionListAPIView.as_view()),
    path('districs/', DistrictListAPIView.as_view()),
    path('user-rud/', UserChangeRole.as_view()),
    path('user-details-rud/', UserDetailRUDAPI.as_view())
]
