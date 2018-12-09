from likes.models import Like
from rest_framework import serializers, fields

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('user', 'post', 'id')
        read_only_fields = ('id', )
