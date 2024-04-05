from rest_framework import serializers
from .models import Blog,Comment
from user.serializer import UserSerializer,ListSerializer
class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer
    like = ListSerializer(many = True)
    class Meta:
        models = Blog
        fields = '__all__'

class BlogWriteSerializer(serializers.ModelSerializer):
    class Meta:
        models = Blog
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = '__all__'