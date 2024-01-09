from django.urls import path

from userapp.views import AppsAPIView, AppsDetailAPIView
from userauth.views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', AppsAPIView.as_view(), name='app-list'),
    path('<str:id>', AppsDetailAPIView.as_view(), name='app-detail')
]
