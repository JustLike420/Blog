from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Tag, Category


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # автоматическое составление url из название
    save_as = True  # после добавления, текст остается
    save_on_top = True  # кнопка сохранения сверху
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')  # какие поля показываются в admin
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # поиск по названию темы
    list_filter = ('category', 'tags')  # фильт по категориям
    read_only_fields = ('views',)

    # вывод фото поста в admin
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title']


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
