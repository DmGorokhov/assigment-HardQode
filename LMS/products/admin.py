from django.contrib import admin

# Register your models here.
from .models import Products, Lessons, LessonsReviews, ProductsLessons, ProductMembers


# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'owner', 'created_at']
    search_fields = ['title', 'description', 'owner', 'created_at']


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductsLessons)
class ProductsLessonsAdmin(admin.ModelAdmin):
    pass


@admin.register(LessonsReviews)
class LessonsReviewsAdmin(admin.ModelAdmin):
    pass
