from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Minyo(models.Model):
    title = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    description = models.TextField()
    audio_file = models.FileField(upload_to='minyo/')
    image = models.ImageField(upload_to='minyo/images/', blank=True, null=True)
    lyrics = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='minyos')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
