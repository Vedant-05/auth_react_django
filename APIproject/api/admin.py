from django.contrib import admin

from .models import Article

# Register your models here.

# admin.site.register(Article)  this is simple way

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_display=('title','description')
    list_filter=('title','description')
