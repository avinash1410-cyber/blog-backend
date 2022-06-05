from django.contrib import admin
from .models import Post,Draft

# Register your models here.
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ("id", "")
admin.site.register(Draft)
admin.site.register(Post)