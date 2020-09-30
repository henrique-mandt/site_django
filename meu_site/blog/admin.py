from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'status')
    list_filter = ('status', 'created_on', 'publish_date', 'author')
    date_hierarchy = 'publish_date'
    raw_id_fields = ('author',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}