from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from rest_framework import generics

from userapp.models import App
from userapp.serializers import UserappSerializer, AdminUserappSerializer, VerifiedAppSerializer

User = get_user_model()


class AppsAPIView(generics.ListCreateAPIView):
    """
    Creates and Lists all apps. Admin sees everything, User sees apps created by user
    Includes verified and unverified apps.
    """
    queryset = App.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        """
        Determines serializer to use
        """
        if self.request.user.is_staff:
            return AdminUserappSerializer
        else:
            return UserappSerializer

    def get_queryset(self):
        """
        Returns all apps if user is staff, else apps created by user
        """
        if not self.request.user.is_staff:
            return self.queryset.filter(owner=self.request.user)
        return self.queryset.all()

    def perform_create(self, serializer):
        """
        Extracts (and saves) owner from the request
        """
        return serializer.save(owner=self.request.user)


class AppsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, updates and deletes an app. Admins can update all apps. User can only update apps they created.
    Users can't update the verified field.
    """
    queryset = App.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_serializer_class(self):
        """
        Determines serializer to use
        """
        if self.request.user.is_staff:
            return AdminUserappSerializer
        else:
            return UserappSerializer

    def get_queryset(self):
        """
        Returns all apps if user is staff, else apps created by user
        """
        if not self.request.user.is_staff:
            return self.queryset.filter(owner=self.request.user)
        return self.queryset.all()


class VerifiedAppsAPIView(generics.ListAPIView):
    """
    Lists all verified apps.
    """
    queryset = App.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = VerifiedAppSerializer

    def get_queryset(self):
        """
        Returns all verified apps.
        """
        return self.queryset.filter(is_verified=True)


class VerifiedAppsDetailAPIView(generics.RetrieveAPIView):
    """
    Retrieves a verified app
    """
    queryset = App.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = VerifiedAppSerializer
    lookup_field = 'id'

    def get_queryset(self):
        """
        Returns all verified apps.
        """
        return self.queryset.filter(is_verified=True)
