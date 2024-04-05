import random
from faker import Faker

class Media:
    def __init__(self, title, release_year, genre, views=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = views
    
    def play(self):
        self.views += 1

class Movie(Media):
    def __str__(self):
        return f"{self.title} ({self.release_year})"

class TVShow(Media):
    def __init__(self, title, release_year, genre, season_number=None, episode_number=None, views=0):
        super().__init__(title, release_year, genre, views)
        self.season_number = season_number
        self.episode_number = episode_number
    
    def __str__(self):
        return f"{self.title} S{self.season_number:02}E{self.episode_number:02}"

def generate_random_movie():
    title = fake.catch_phrase()
    release_year = random.randint(1950, 2022)
    genre = fake.random_element(elements=("Action", "Comedy", "Drama", "Horror", "Sci-Fi"))
    return Movie(title, release_year, genre)

def generate_random_tvshow():
    title = fake.catch_phrase()
    release_year = random.randint(1950, 2022)
    genre = fake.random_element(elements=("Action", "Comedy", "Drama", "Horror", "Sci-Fi"))
    season_number = random.randint(1, 20)
    episode_number = random.randint(1, 32)
    return TVShow(title, release_year, genre, season_number, episode_number)

def get_movies(library):
    movies = [media for media in library if isinstance(media, Movie)]
    return sorted(movies, key=lambda x: x.title)

def get_series(library):
    series = [media for media in library if isinstance(media, TVShow)]
    return sorted(series, key=lambda x: x.title)

def search(library, title):
    results = [media for media in library if title.lower() in media.title.lower()]
    return results

def generate_views(library):
    random_media = random.choice(library)
    views = random.randint(1, 100)
    random_media.views += views

def run_generate_views(library, times=10):
    for _ in range(times):
        generate_views(library)

def top_titles(library, content_type, num_titles=5):
    if content_type == 'movies':
        filtered_library = [media for media in library if isinstance(media, Movie)]
    elif content_type == 'series':
        filtered_library = [media for media in library if isinstance(media, TVShow)]
    else:
        raise ValueError("Nieprawidłowy typ treści. Wybierz 'movies' lub 'series'.")
    
    sorted_library = sorted(filtered_library, key=lambda x: x.views, reverse=True)
    top_titles = [media.title for media in sorted_library][:num_titles]
    return top_titles
    
# Generowanie biblioteki filmów i seriali
library = []

fake = Faker()
for _ in range(10):  # Generujemy po 10 losowych filmów i seriali
    library.append(generate_random_movie())
    library.append(generate_random_tvshow())

# Testowanie funkcji
movies = get_movies(library)
print("Biblioteka filmów:")
for movie in movies:
    print(movie)

print("\nBiblioteka seriali:")
series = get_series(library)
for serial in series:
    print(serial)

run_generate_views(library)
print("\nPo wygenerowaniu odtworzeń:")
for media in library:
    print(f"{media.title}: {media.views} odtworzeń")

print("\nNajpopularniejsze filmy:")
print(top_titles(library, 'movies'))

print("\nNajpopularniejsze seriale:")
print(top_titles(library, 'series'))
