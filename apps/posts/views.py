from rest_framework import viewsets
from posts.serializers import PostSerializer
from posts.models import Post
from dry_rest_permissions.generics import DRYPermissions


class PostsViewSet(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer