from django.urls import path
from .views import ProductsView, UserLessonsView, UserLessonsByProductView

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='products_list'),
    path('lessons/<int:user_id>', UserLessonsView.as_view(), name='user_lessons'),
    path('<path:product_title>/lessons/<int:user_id>', UserLessonsByProductView.as_view(),
         name='user_lessons_by_product'),
]
