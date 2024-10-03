import requests
import pandas as pd

API_KEY = '172c6a9faffa1091decf5ce31be741a3'  # 在 TMDb 註冊後獲得
BASE_URL = 'https://api.themoviedb.org/3'

# 函數：抓取 TMDb 資料
def get_popular_movies(pages):
    movies = []
    for page in range(1, pages + 1):
        url = f'{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page={page}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for movie in data['results']:
                movies.append({
                    'title': movie['title'],
                    'rating': movie['vote_average'],
                    'genre_ids': movie['genre_ids']
                })
        else:
            raise Exception(f"抓取資料時發生錯誤：{response.status_code}")
    return movies

# 函數：獲取電影類型
def get_genres():
    url = f'{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US'
    response = requests.get(url)
    if response.status_code == 200:
        return {genre['id']: genre['name'] for genre in response.json()['genres']}
    else:
        raise Exception(f"獲取類型資料時發生錯誤：{response.status_code}")

# 函數：抓取並保存資料
def fetch_and_save_data(pages):
    movies = get_popular_movies(pages)
    genres = get_genres()

    # 將 genre_ids 轉換為類型名稱
    for movie in movies:
        movie['genres'] = [genres[genre_id] for genre_id in movie['genre_ids'] if genre_id in genres]

    # 將數據轉換為 DataFrame 並保存為 CSV 文件
    movies_df = pd.DataFrame(movies)
    movies_df.to_csv('data/tmdb_popular_movies.csv', index=False)

    return 'data/tmdb_popular_movies.csv'