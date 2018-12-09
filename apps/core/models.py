from django.db import models


class BasePermissionsModel(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_retrieve_permission(request):
        return True

    def has_object_retrieve_permission(self, request):
        return True

    @staticmethod
    def has_update_permission(request):
        return True

    def has_object_update_permission(self, request):
        return self.user == request.user

    @staticmethod
    def has_destroy_permission(request):
        return True

    def has_object_destroy_permission(self, request):
        return self.user == request.user

    @staticmethod
    def has_write_permission(request):
        return True

    def has_object_write_permission(self, request):
        return self.user == request.user

    @staticmethod
    def has_create_permission(request):
        return True

    def has_object_create_permission(self, request):
        return self.user == request.user