# Generated by Django 4.2.5 on 2023-09-21 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productslessons_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonsreviews',
            name='poduct_members_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productmembers'),
        ),
    ]