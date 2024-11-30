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

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's not already set
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            # Loop to ensure uniqueness
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            self.slug = slug

        # Call the parent class's save method
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
