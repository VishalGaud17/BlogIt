from django.contrib import admin
from blogapp.models import blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','blog','is_active']

admin.site.register(blog,BlogAdmin)
