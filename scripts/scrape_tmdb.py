import requests
import pandas as pd

def fetch_data_from_api(pages):
    api_key = '172c6a9faffa1091decf5ce31be741a3'  # 替換為你自己的 TMDb API 密鑰
    base_url = 'https://api.themoviedb.org/3/movie/popular'
    genre_url = 'https://api.themoviedb.org/3/genre/movie/list'
    
    # 先抓取所有的電影類型名稱
    genre_response = requests.get(genre_url, params={'api_key': api_key, 'language': 'en-US'})
    genres = genre_response.json().get('genres', [])
    genre_dict = {genre['id']: genre['name'] for genre in genres}  # 建立類型ID和名稱的對應字典

    all_movies = []

    for page in range(1, pages + 1):
        params = {
            'api_key': api_key,
            'language': 'en-US',
            'page': page
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            movies = data.get('results', [])
            for movie in movies:
                # 將電影類型ID轉換為名稱，如果有多個類型，用逗號分隔
                genre_names = ', '.join([genre_dict.get(genre_id, 'Unknown') for genre_id in movie.get('genre_ids', [])])
                all_movies.append({
                    'title': movie['title'],
                    'rating': movie['vote_average'],
                    'genre': genre_names  # 顯示類型名稱而非ID
                })
        else:
            print(f"Failed to fetch data from page {page}. Status code: {response.status_code}")

    # 將數據轉換為DataFrame，並返回
    df = pd.DataFrame(all_movies)
    return df

