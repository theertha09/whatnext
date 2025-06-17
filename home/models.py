from django.db import models

class VoiceOfSuccess(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='media/voice_of_success/')
    thumbnail = models.ImageField(upload_to='media/thumbnails/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    alt_video_text = models.TextField(max_length=300, null=True, blank=True)
    alt_video_title = models.TextField(max_length=300, null=True, blank=True)
    alt_video_caption = models.TextField(max_length=300, null=True, blank=True)
    alt_video_description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class StudentReview(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    review = models.TextField()
    country = models.CharField(max_length=100)
    date = models.DateField()
    profile_image = models.ImageField(upload_to='media/review_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class MetaTagsHome(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    canonical_url = models.URLField(null=True, blank=True)
    h1_tag = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    word_count = models.IntegerField(null=True, blank=True)
    internal_links = models.TextField(null=True, blank=True)  
    external_links = models.TextField(null=True, blank=True)
    anchor_text = models.CharField(max_length=255, null=True, blank=True)
    schema_type = models.CharField(max_length=255, null=True, blank=True)
    json_ld_schema = models.TextField(null=True, blank=True)
    structured_schema = models.TextField(null=True, blank=True)
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    og_image = models.ImageField(upload_to='media/seo_home_images/', null=True, blank=True)
    twitter_card = models.CharField(max_length=50, null=True, blank=True)
    twitter_title = models.CharField(max_length=255, null=True, blank=True)
    twitter_description = models.TextField(null=True, blank=True)
    twitter_image = models.ImageField(upload_to='media/seo_home_images/', null=True, blank=True)
    noindex = models.BooleanField(default=False)  
    nofollow = models.BooleanField(default=False)
    amp_enabled = models.BooleanField(default=False)
    lazy_load_images = models.BooleanField(default=False)  

    def __str__(self):
        return self.title or "MetaTagshome Entry"