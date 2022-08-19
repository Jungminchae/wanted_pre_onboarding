from rest_framework.permissions import BasePermission
from apis.models import User


class IsCompanyUser(BasePermission):
    def has_permission(self, request, view):
        user_id = request.data["user"]
        user = User.objects.filter(id=user_id)
        if user.exists():
            return user.first().is_company is True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user_id = request.data["user"]
        user = User.objects.filter(id=user_id)
        if user.exists():
            return user.first().id == obj.user.id
        return False
