from django.contrib import admin

from .models import Announcement, Category, Subcategory


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'price', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('type', 'price')
    list_filter = ('type', )
    search_fields = ('title', 'description')


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Announcement, AnnouncementAdmin)