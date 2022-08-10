from rest_framework import serializers

from applications.cinema.models import Category, Cinema, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class CinemaSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=False, read_only=True)
    class Meta:
        model = Cinema
        fields = '__all__'



