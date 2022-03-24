# Generated by Django 3.2.9 on 2021-11-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20211122_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='ram_category',
            field=models.CharField(choices=[('4GB', '4GB'), ('8GB', '8GB')], default='4GB', max_length=100),
        ),
        migrations.AlterField(
            model_name='variation',
            name='storage_category',
            field=models.CharField(choices=[('HDD', 'HDD'), ('SSD', 'SSD')], default='HDD', max_length=100),
        ),
    ]