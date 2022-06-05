from .models import Post,Draft,User
# import serializer from rest_framework
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class DraftSerializer(serializers.ModelSerializer):
    author=AccountSerializer()
    class Meta:
        model = Draft
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    post=DraftSerializer()
    class Meta:
        model = Post
        fields = "__all__"
