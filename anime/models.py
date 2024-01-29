from django.db import models

# Create your models here.
class Genre(models.Model):
    genre_data = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.genre_data}"
    
class Anime(models.Model):
    title = models.CharField(max_length=100)
    studio = models.CharField(max_length=100)
    episodes = models.IntegerField(blank=True, null=True)
    genre = models.ManyToManyField(Genre, related_name="anime")

    def __str__(self):
        return f"Anime {self.id}: {self.title}({self.studio})"
    
    