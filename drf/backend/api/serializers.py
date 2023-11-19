# Django itself checks the user and imports it automatically.This method is good for when you have created a
# personalized user model.
from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

