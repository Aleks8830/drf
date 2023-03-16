'ФАИЛ ДЛЯ ОГРАНИЧЕНИЯ ДОСТУПА'
from rest_framework import permissions


class IsAdmninRedOnly(permissions.BasePermission):
    def has_permission(self,request,view):   #огрничение прав доступа на уровне всег запроса#
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user