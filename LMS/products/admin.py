from django.contrib import admin

# Register your models here.
from .models import (Products, Lessons, LessonsReviews,
                     ProductsLessons, ProductMembers)


# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'owner', 'created_at']
    search_fields = ['title', 'description', 'owner', 'created_at']


@admin.register(ProductMembers)
class ProductMembersAdmin(admin.ModelAdmin):
    list_display = ['get_product_title', 'get_user_name']

    @admin.display(description='Product Title')
    def get_product_title(self, obj):
        return obj.product.title

    @admin.display(description='User Name')
    def get_user_name(self, obj):
        return obj.member.username


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductsLessons)
class ProductsLessonsAdmin(admin.ModelAdmin):
    list_display = ['get_product_title', 'get_lesson_name']

    @admin.display(description='Product Title')
    def get_product_title(self, obj):
        return obj.product.title

    @admin.display(description='Lesson')
    def get_lesson_name(self, obj):
        return obj.lesson.name


@admin.register(LessonsReviews)
class LessonsReviewsAdmin(admin.ModelAdmin):
    list_display = ['get_lesson_name', 'get_user_name', 'lesson_duration_sec',
                    'lesson_view_duration_sec', 'viewing_status',
                    'get_product_name']

    @admin.display(description='Lesson Name')
    def get_lesson_name(self, obj):
        return obj.lesson.name

    @admin.display(description='Product Name')
    def get_product_name(self, obj):
        return obj.product.title

    @admin.display(description='User Name')
    def get_user_name(self, obj):
        return obj.user.username
