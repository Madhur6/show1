from django.contrib import admin
from .models import Genre, Anime

# Register your models here.
admin.site.register(Genre)

@admin.register(Anime)
class Admin(admin.ModelAdmin):
    list_display = (
        "title",
        "studio",
        "episodes"
    )

    list_per_page = 10