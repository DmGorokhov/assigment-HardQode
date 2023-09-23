from rest_framework import serializers
from .models import LessonsReviews


class ProductsSerializer(serializers.Serializer):
    product = serializers.CharField(source='product__title')
    lesson_count = serializers.IntegerField()
    user_count = serializers.IntegerField()
    total_view_duration_sec = serializers.IntegerField()


class UserLessonsSerializer(serializers.ModelSerializer):
    lesson = serializers.CharField(source='lesson__name')
    user = serializers.CharField(source='user__username')

    class Meta:
        model = LessonsReviews
        fields = ['user', 'lesson',
                  'lesson_view_duration_sec', 'viewing_status']


class UserProductsLessonsSerializer(serializers.ModelSerializer):
    lesson = serializers.CharField(source='lesson__name')
    user = serializers.CharField(source='user__username')
    product = serializers.CharField(source='product__title')
    last_viewed = serializers.DateTimeField(source='updated_at',
                                            format='%b %d, %Y %I:%M %p')

    class Meta:
        model = LessonsReviews
        fields = ['product', 'user',
                  'lesson', 'lesson_view_duration_sec',
                  'viewing_status', 'last_viewed']
