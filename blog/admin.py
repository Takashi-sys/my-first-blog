from django.contrib import admin
from .models import Post,Comment  # Commentを追加

admin.site.register(Post)
admin.site.register(Comment) # Commentを追加

# Register your models here.
