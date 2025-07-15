from django.db import models

class Contact(models.Model):
    FINDUS_CHOICES = [
        ('Facebook','Facebook'),
        ('Telegram','Telegram'),
        ('Instagram','Instagram'),
        ('Other','Other'),
        ('LinkedIn','LinkedIn'),
        ('Reference','Reference'),
        ('Google','Google'),
    ]

    find_us = models.CharField(max_length=10, choices=FINDUS_CHOICES)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.TextField()

    def __str__(self):
        return self.name

class MetaTagsContact(models.Model):
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
    og_image = models.ImageField(upload_to='media/seo_contact_images/', null=True, blank=True)
    twitter_card = models.CharField(max_length=50, null=True, blank=True)
    twitter_title = models.CharField(max_length=255, null=True, blank=True)
    twitter_description = models.TextField(null=True, blank=True)
    twitter_image = models.ImageField(upload_to='media/seo_contact_images/', null=True, blank=True)
    noindex = models.BooleanField(default=False)  
    nofollow = models.BooleanField(default=False)
    amp_enabled = models.BooleanField(default=False)
    lazy_load_images = models.BooleanField(default=False)  

    def __str__(self):
        return self.title or "MetaTagscontact Entry"
