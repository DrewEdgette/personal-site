from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    author = models.CharField(max_length=100, default="Drew Edgette")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    reading_time = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate slug if not set
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            # Loop to ensure uniqueness
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        # Calculate reading time based on word count at 220 words/minute
        words = self.content.split()
        word_count = len(words)
        
        self.reading_time = int(word_count / 220)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title