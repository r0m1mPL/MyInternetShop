# Generated by Django 4.0.1 on 2022-01-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_mailinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='shop/images/standart.jpeg', upload_to='shop/images/', verbose_name='Image'),
        ),
    ]