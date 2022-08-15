from rest_framework import serializers

from applications.cinema.models import Category, Cinema, Preview, Comment, Favorite


class PreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preview
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation ['favorite'] == False:
            representation.clear()
        return representation




class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    images = PreviewSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Cinema
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        images = requests.FILES

        cinema = Preview.objects.create(**validated_data)
        for image in images.getlist('images'):
            Preview.objects.create(cinema=cinema, image=image)

        return cinema
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['like'] = instance.likes.filter(like=True).count()

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






