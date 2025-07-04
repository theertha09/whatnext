# Generated by Django 4.2 on 2025-06-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaTagsHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('meta_keywords', models.TextField(blank=True, null=True)),
                ('canonical_url', models.URLField(blank=True, null=True)),
                ('h1_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('word_count', models.IntegerField(blank=True, null=True)),
                ('internal_links', models.TextField(blank=True, null=True)),
                ('external_links', models.TextField(blank=True, null=True)),
                ('anchor_text', models.CharField(blank=True, max_length=255, null=True)),
                ('schema_type', models.CharField(blank=True, max_length=255, null=True)),
                ('json_ld_schema', models.TextField(blank=True, null=True)),
                ('structured_schema', models.TextField(blank=True, null=True)),
                ('og_title', models.CharField(blank=True, max_length=255, null=True)),
                ('og_description', models.TextField(blank=True, null=True)),
                ('og_image', models.ImageField(blank=True, null=True, upload_to='media/seo_home_images/')),
                ('twitter_card', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter_title', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_description', models.TextField(blank=True, null=True)),
                ('twitter_image', models.ImageField(blank=True, null=True, upload_to='media/seo_home_images/')),
                ('noindex', models.BooleanField(default=False)),
                ('nofollow', models.BooleanField(default=False)),
                ('amp_enabled', models.BooleanField(default=False)),
                ('lazy_load_images', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('review', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='media/review_images/')),
            ],
        ),
        migrations.CreateModel(
            name='VoiceOfSuccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='media/voice_of_success/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='media/thumbnails/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('alt_video_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_video_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_video_caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_video_description', models.TextField(blank=True, max_length=300, null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
