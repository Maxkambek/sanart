from django.urls import path, include

urlpatterns = [
    path('contents/', include('contents.urls')),
    path('main/', include('main.urls')),
    path('accounts/', include('accounts.urls'))
]
