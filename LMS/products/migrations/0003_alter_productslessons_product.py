# Generated by Django 4.2.5 on 2023-09-21 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productslessons',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.products'),
        ),
    ]
