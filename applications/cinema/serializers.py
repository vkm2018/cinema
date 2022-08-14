from rest_framework import serializers

from applications.cinema.models import Category, Cinema, Image, Comment


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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['like'] = instance.likes.filter(like=True).count()
        representation['favorite'] = instance.favorits.filter(favorite=True).count()
        rating_result = 0
        for rating in instance.ratings.all():
            rating_result += int(rating.rating)
        try:
            representation['rating'] = rating_result / instance.ratings.all().count()
        except ZeroDivisionError:
            pass

        return representation


class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = '__all__'

# class FavoriteSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Favorite
#         fields = '__all__'