from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


# Create your models here.
class Products(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255,
                             null=False, unique=True,
                             )
    description = models.TextField('description', null=True, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                              related_name='owner',
                              verbose_name='owner'
                              )
    created_at = models.DateTimeField("created_at", auto_now_add=True)

    def __str__(self):
        return self.title


class ProductMembers(models.Model):
    product = models.ForeignKey(Products, on_delete=models.PROTECT, null=False)
    member = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField("created_at", auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'member'],
                                    name='unique_product_member')
        ]


class Lessons(models.Model):
    name = models.CharField(verbose_name='name', max_length=255,
                            null=False, unique=True)
    content_src_link = models.URLField(max_length=200)
    playback_duration_sec = models.PositiveIntegerField()
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    products = models.ManyToManyField(Products, through='ProductsLessons',
                                      related_name='lessons',
                                      verbose_name='lessons',
                                      )

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.playback_duration_sec == 0:
            raise ValidationError("Value must be greater than 0")


class ProductsLessons(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'lesson'],
                                    name='unique_product_lesson')
        ]


class LessonsReviews(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, null=False,
                               verbose_name='lesson_id')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    lesson_duration_sec = models.PositiveIntegerField()
    lesson_view_duration_sec = models.PositiveIntegerField(default=0)
    viewing_status = models.CharField(verbose_name='viewing_status',
                                      max_length=50, null=False,
                                      default="Не просмотрено")
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['lesson', 'user'],
                                    name='unique_lesson_user')
        ]

    def save(self, *args, **kwargs):
        lesson_is_viewed_mark = 0.8
        if self.lesson_view_duration_sec >= \
                lesson_is_viewed_mark * self.lesson_duration_sec:
            self.viewing_status = "Просмотрено"
        super().save(*args, **kwargs)
