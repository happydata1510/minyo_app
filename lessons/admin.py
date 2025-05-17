from django.contrib import admin
from .models import Lesson, UserRecording, LessonGroup

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

@admin.register(LessonGroup)
class LessonGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'order', 'created_at')
    list_filter = ('group',)
    search_fields = ('title', 'description')
    list_editable = ('order',)

@admin.register(UserRecording)
class UserRecordingAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'created_at')
    list_filter = ('user', 'lesson')
