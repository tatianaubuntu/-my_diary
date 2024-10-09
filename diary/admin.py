from django.contrib import admin

from diary.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'owner',)
    list_filter = ('title', 'created_at', 'updated_at', )
    search_fields = ('title', 'body', )
