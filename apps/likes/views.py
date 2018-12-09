from likes.models import Like
from likes.serializers import LikeSerializer
from rest_framework import viewsets
from dry_rest_permissions.generics import DRYPermissions


class LikesViewSet(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
