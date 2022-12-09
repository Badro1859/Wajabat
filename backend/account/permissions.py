

from rest_framework import permissions


class OwnerOrCreateOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        # print('user auth : ', request.user.is_authenticated)
        # print('request header auth', request.headers.get('Authorization'))
        
        ## authenticated user can not create account
        if request.user.is_authenticated:
            return request.method != 'POST'

        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):

        ## only owner can modifie it's data 
        return request.user.is_authenticated and obj.pk == request.user.pk
        