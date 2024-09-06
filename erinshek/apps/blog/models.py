from django.db import models
from apps.account.models import Account


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='my_blogs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
