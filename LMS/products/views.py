from .models import LessonsReviews
from rest_framework.generics import ListAPIView
from .serializers import (UserLessonsSerializer, UserProductsLessonsSerializer,
                          ProductsSerializer)
from django.db.models import Count, Sum


# Create your views here.
class ProductsView(ListAPIView):
    serializer_class = ProductsSerializer

    queryset = LessonsReviews.objects.values('product__title') \
        .annotate(lesson_count=Count('lesson', distinct=True)) \
        .annotate(user_count=Count('user', distinct=True)) \
        .annotate(total_view_duration_sec=Sum('lesson_view_duration_sec'))


class UserLessonsView(ListAPIView):
    serializer_class = UserLessonsSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return LessonsReviews.objects.filter(user=user_id). \
            values('user__username', 'lesson__name',
                   'lesson_view_duration_sec', 'viewing_status')


class UserLessonsByProductView(ListAPIView):
    serializer_class = UserProductsLessonsSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        product_title = self.kwargs['product_title']
        return LessonsReviews.objects. \
            filter(user=user_id). \
            filter(product__title=product_title). \
            values('user__username', 'product__title', 'lesson__name',
                   'lesson_view_duration_sec', 'viewing_status', 'updated_at')
