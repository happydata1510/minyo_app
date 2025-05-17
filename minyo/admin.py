from django.contrib import admin
from .models import Category, Minyo

class MinyoAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'category', 'created_at')
    list_filter = ('region', 'category')
    search_fields = ('title', 'description', 'lyrics')

admin.site.register(Category)
admin.site.register(Minyo, MinyoAdmin)
