import random
from faker import Faker
from datetime import datetime

class Media:
    def __init__(self, title, release_year, views=0):
        self.title = title
        self.release_year = release_year
        self.views = views
    
    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    def __lt__(self, other):
        return self.title < other.title

class TVShow(Media):
    def __init__(self, title, release_year, season_number, episode_number):
        super().__init__(title, release_year)
        self.season_number = season_number
        self.episode_number = episode_number
    
    def __str__(self):
        if self.season_number is not None and self.episode_number is not None:
            return f"{self.title} S{self.season_number:02}E{self.episode_number:02} ({self.release_year})"
        else:
            return f"{self.title} ({self.release_year})"

def generate_random_movie():
    fake = Faker()
    title = fake.catch_phrase()
    release_year = random.randint(1950, 2024)
    return Media(title, release_year)

def generate_random_tvshow():
    fake = Faker()
    title = fake.catch_phrase()
    release_year = random.randint(1950, 2024)
    season_number = random.randint(1, 20)
    episode_number = random.randint(1, 32)
    return TVShow(title, release_year, season_number, episode_number)

def get_movies_and_series(library):
    movies = [media for media in library if isinstance(media, Media)]
    series = [media for media in library if isinstance(media, TVShow)]
    return sorted(movies, key=lambda x: x.title), sorted(series, key=lambda x: x.title)

def generate_views(library):
    for media in library:
        views = random.randint(1, 100)
        media.views += views

def run_generate_views(library):
    for _ in range(10):
        generate_views(library)

def top_titles(library, content_type, num_titles=5):
    if content_type == 'movies':
        filtered_library = [media for media in library if isinstance(media, Media)]
    elif content_type == 'series':
        filtered_library = [media for media in library if isinstance(media, TVShow)]
    else:
        raise ValueError("Nieprawidłowy typ treści. Wybierz 'movies' lub 'series'.")
    
    sorted_library = sorted(filtered_library, key=lambda x: x.views, reverse=True)
    top_titles = [media.title for media in sorted_library][:num_titles]
    return top_titles

if __name__ == "__main__":
    library = []

    for _ in range(10): 
        library.append(generate_random_movie())
        library.append(generate_random_tvshow())

    movies, series = get_movies_and_series(library)

    print("Biblioteka filmów:")
    for movie in movies:
        print(movie)

    print("\nBiblioteka seriali:")
    for serial in series:
        print(serial)

    run_generate_views(library)
    print("\nLiczba odtworzeń:")
    for media in library:
        print(f"{media.title}: {media.views} odtworzeń")

    print(f"\nNajpopularniejsze filmy i seriale dnia {datetime.now().strftime('%d.%m.%Y')}:")
    print("Top 3 najpopularniejsze filmy:")
    print(top_titles(library, 'movies')[:3])
    print("Top 3 najpopularniejsze seriale:")
    print(top_titles(library, 'series')[:3])
