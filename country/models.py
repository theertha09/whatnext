from django.db import models
from django.utils.text import slugify

class Countries(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = models.ImageField(upload_to="media/country_image/")
    icon = models.ImageField(upload_to="media/country_icon/")
    description = models.TextField()
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or Countries.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.title) if self.title else "blogcard-section"
        # Trim the slug to a maximum of 50 characters and ensure it does not cut off mid-word
        base_slug = self._trim_slug(base_slug, max_length=30)
        slug = base_slug
        counter = 1
        while Countries.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def _trim_slug(self, slug, max_length):
        if len(slug) <= max_length:
            return slug
        truncated_slug = slug[:max_length]
        # Ensure we don't cut off a word
        if truncated_slug[-1] != '-' and slug[max_length] != '-':
            last_hyphen = truncated_slug.rfind('-')
            if last_hyphen != -1:
                truncated_slug = truncated_slug[:last_hyphen]
        return truncated_slug.rstrip(':')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/{self.slug}/"
    
    
class University(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="media/university_logo/")
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name="universities")

    def __str__(self):
        return self.title


class WhyChoose(models.Model):  
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to="media/whychooseus_icon/")
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name="why_choose_reasons")

    def __str__(self):
        return self.title
    
class MetaTagsCountry(models.Model):
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
    og_image = models.ImageField(upload_to='media/seo_country_images/', null=True, blank=True)
    twitter_card = models.CharField(max_length=50, null=True, blank=True)
    twitter_title = models.CharField(max_length=255, null=True, blank=True)
    twitter_description = models.TextField(null=True, blank=True)
    twitter_image = models.ImageField(upload_to='media/seo_country_images/', null=True, blank=True)
    noindex = models.BooleanField(default=False)  
    nofollow = models.BooleanField(default=False)
    amp_enabled = models.BooleanField(default=False)
    lazy_load_images = models.BooleanField(default=False)  

    def __str__(self):
        return self.title or "MetaTagscountry Entry"