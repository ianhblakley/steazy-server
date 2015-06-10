from django.contrib import admin

# Register your models here.
from mobile.models import Song, Playlist, Song_to_Playlist


class SongsInline(admin.TabularInline):
    model = Song_to_Playlist
    fields = ['song', 'added_by']
    extra = 0


class PlaylistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'owner']}),
    ]
    inlines = [SongsInline]


admin.site.register(Song)
admin.site.register(Playlist, PlaylistAdmin)
