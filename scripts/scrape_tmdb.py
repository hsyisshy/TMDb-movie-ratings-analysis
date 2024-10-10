import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#function to fetch data from the API
def fetch_data_from_api(pages):
    api_key = os.getenv('TMDB_API_KEY')  # Fetch the API key from the environment variables
    base_url = 'https://api.themoviedb.org/3/movie/popular'  # URL for fetching popular movies
    genre_url = 'https://api.themoviedb.org/3/genre/movie/list'  # URL for fetching all movie genres
    
    # Fetch all movie genre names first
    genre_response = requests.get(genre_url, params={'api_key': api_key, 'language': 'en-US'})
    genres = genre_response.json().get('genres', [])  # Get genres from the response
    genre_dict = {genre['id']: genre['name'] for genre in genres}  # Create a dictionary mapping genre IDs to names

    all_movies = []  # List to store all movie data

    # Loop through the specified number of pages to fetch movies
    for page in range(1, pages + 1):
        params = {
            'api_key': api_key,
            'language': 'en-US',
            'page': page
        }
        response = requests.get(base_url, params=params)  # Make the API request
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            movies = data.get('results', [])  # Get the list of movies
            for movie in movies:
                # Convert genre IDs to names, using a comma to separate multiple genres
                genre_names = ', '.join([genre_dict.get(genre_id, 'Unknown') for genre_id in movie.get('genre_ids', [])])
                # Append movie data to the list
                all_movies.append({
                    'title': movie['title'],  # Movie title
                    'rating': movie['vote_average'],  # Movie rating
                    'genre': genre_names  # Display genre names instead of IDs
                })
        else:
            print(f"Failed to fetch data from page {page}. Status code: {response.status_code}")  # Handle request failure

    # Convert the list of movies to a DataFrame and return
    df = pd.DataFrame(all_movies)
    return df


