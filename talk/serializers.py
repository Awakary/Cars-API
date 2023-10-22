from rest_framework import serializers
from .models import Car, Country, Comment, Producter


class CountrySerializer(serializers.ModelSerializer):
    producters = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['id', 'name', 'producters']


class CarSerializer(serializers.ModelSerializer):
    producter = serializers.StringRelatedField()
    comments = serializers.StringRelatedField(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    def get_comments_count(self, obj):
        return Comment.objects.filter(car_id=obj.id).count()
    class Meta:
        model = Car
        fields = ['id', 'name', 'producter', 'start_year', 'last_year', 'comments', 'comments_count']
class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarForProducterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return Comment.objects.filter(car_id=obj.id).count()

    class Meta:
        model = Car
        fields = ['name', 'comments_count']


class ProducterSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(read_only=True)
    cars = CarForProducterSerializer(many=True, read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Producter
        fields = ['id', 'name', 'country', 'cars', 'comments']

class ProducterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producter
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'author_email', 'car', 'date_created', 'text']



class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author_email', 'car', 'date_created', 'text']


    def validate(self, comment):
        text = comment['text']
        if text.isdigit():
            raise serializers.ValidationError('Нельзя вводить только цифры, введите пожалуйста текст')
        return comment