# Generated by Django 2.1.7 on 2019-03-26 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_book_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_url',
            field=models.CharField(default='book_generic.jpeg', max_length=250),
        ),
    ]