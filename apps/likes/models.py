import uuid
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from core.models import BasePermissionsModel


class Like(BasePermissionsModel):
    class Meta:
        unique_together = (('user', 'post'),)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
