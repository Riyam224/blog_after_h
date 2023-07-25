from django.db import models

from django.contrib.auth.models import User

STATUS = (
    ('Draft', 'Draft'),
    ('Publish', 'Publish')
)


class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here
    
    title  = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True , null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name='blog_posts')
    updated_on  = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS , max_length=10,  default='Draft')
    
   
    class Meta:
        ordering = ['-created_on']
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title
