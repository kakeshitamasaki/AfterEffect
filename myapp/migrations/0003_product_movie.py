# Generated by Django 4.0 on 2022-11-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='movie',
            field=models.FileField(blank=True, upload_to='images'),
        ),
    ]
