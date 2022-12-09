from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator


from rest_framework import generics, viewsets, permissions, authentication
from rest_framework.response import Response
from rest_framework import status 

from account.models import User
from account.serializers import UserSerializer
from account.permissions import OwnerOrCreateOnly


## view for create sinup
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [OwnerOrCreateOnly]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        user = self.request.user
        if self.action == "list" and not user.is_staff:
            queryset = queryset.filter(pk=user.id)

        return queryset

