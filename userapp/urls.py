from django.urls import path

from userapp.views import AppsAPIView, AppsDetailAPIView, VerifiedAppsAPIView, VerifiedAppsDetailAPIView


urlpatterns = [
    path('', AppsAPIView.as_view(), name='app-list'),
    path('<str:id>', AppsDetailAPIView.as_view(), name='app-detail'),
    path('verified/', VerifiedAppsAPIView.as_view(), name='verified-app-list'),
    path('verified/<str:id>', VerifiedAppsDetailAPIView.as_view(), name='verified-app-detail'),
]
