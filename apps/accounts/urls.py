from django.urls import path
from .views import LoginAPI, RegisterAPI, RegisterConfirmAPI, ChangePasswordAPI, RegionListAPIView, \
    DistrictListAPIView, UserChangeRole, UserDetailYurudikCreateAPIView, UserDetailJismoniyRUDAPI, LoginVerifyAPIView, \
    UserDetailJismoniyCreateAPIView,UserDetailYuridikRUDAPI

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('login-verify/', LoginVerifyAPIView.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('register-confirm/', RegisterConfirmAPI.as_view()),
    path('regions/', RegionListAPIView.as_view()),
    path('districs/', DistrictListAPIView.as_view()),
    path('user-rud/', UserChangeRole.as_view()),
    path('user-details-rud-jismoniy/', UserDetailJismoniyRUDAPI.as_view()),
    path('user-details-rud-yurudik/', UserDetailYuridikRUDAPI.as_view()),
    path('user-details-create-yurudik/', UserDetailYurudikCreateAPIView.as_view()),
    path('user-details-create-jismoniy/', UserDetailJismoniyCreateAPIView.as_view()),
]
