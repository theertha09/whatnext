# Generated by Django 4.2 on 2025-06-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/country_icon/'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/country_image/'),
        ),
        migrations.AlterField(
            model_name='university',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/university_logo/'),
        ),
        migrations.AlterField(
            model_name='whychoose',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/whychooseus_icon/'),
        ),
    ]
