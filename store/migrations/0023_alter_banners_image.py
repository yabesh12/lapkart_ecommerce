# Generated by Django 3.2.9 on 2021-11-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_banners_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banners',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/banners'),
        ),
    ]