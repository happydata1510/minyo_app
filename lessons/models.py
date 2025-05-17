from django.db import models
from django.contrib.auth.models import User

class LessonGroup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='lessons/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Lesson(models.Model):
    group = models.ForeignKey(LessonGroup, on_delete=models.CASCADE, related_name='lessons', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='lessons/')
    commentary = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='lessons/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=1)  # 강의 순서
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']  # 순서대로 정렬

class UserRecording(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recordings')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_recordings')
    recording_file = models.FileField(upload_to='recordings/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}의 {self.lesson.title} 녹음"
