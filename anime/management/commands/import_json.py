from django.core.management.base import BaseCommand
from anime.models import Anime, Genre
import json

class Command(BaseCommand):
    help = 'Load Json data into our models'

    def handle(self, *args, **kwargs):
        try:
            with open('anime/fixtures/json_data.json', 'r', encoding='utf8') as file:
                data = json.load(file)

                for item in data.get('animes', []):
                    title = item.get('title')
                    studio = item.get('studio')
                    episodes = int(item.get('episodes'))
                    
                    genre_data = item.get('genre', [])
                    genre = [Genre.objects.get_or_create(genre_data=genre)[0] for genre in genre_data]

                    anime_instance = Anime.objects.create(
                        title=title,
                        studio=studio,
                        episodes=episodes,
                    )

                    anime_instance.genre.set(genre)

            self.stdout.write(self.style.SUCCESS("Successfully loaded data!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occured: {e}'))