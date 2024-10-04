import os
import matplotlib
matplotlib.use('Agg')  # Use 'Agg' backend to avoid GUI issues
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

def plot_rating_distribution(data):
    plt.figure(figsize=(20, 15))  # 調整圖表尺寸
    plt.hist(data['rating'], bins=20, color='blue', edgecolor='black')
    plt.title('Rating Distribution', fontsize=40)  # 調整標題字體
    plt.xlabel('Rating', fontsize=30)  # 調整 X 軸標籤字體
    plt.ylabel('Frequency', fontsize=30)  # 調整 Y 軸標籤字體
    plt.xticks(fontsize=25)  # 調整 X 軸刻度字體
    plt.yticks(fontsize=25)  # 調整 Y 軸刻度字體

    save_path = os.path.join('visualizations', 'rating_distribution.png')
    return save_plot_to_base64(save_path)

def plot_genre_avg_rating(data):
    genre_ratings = data.groupby('genre')['rating'].mean().sort_values()
    plt.figure(figsize=(15, 10))  # 調整圖表尺寸
    genre_ratings.plot(kind='barh', color='green')
    plt.title('Average Rating by Genre', fontsize=30)  # 調整標題字體
    plt.xlabel('Average Rating', fontsize=20)  # 調整 X 軸標籤字體
    plt.ylabel('Genre', fontsize=20)  # 調整 Y 軸標籤字體
    plt.xticks(fontsize=16)  # 調整 X 軸刻度字體
    plt.yticks(fontsize=16)  # 調整 Y 軸刻度字體

    save_path = os.path.join('visualizations', 'genre_avg_rating.png')
    return save_plot_to_base64(save_path)

def plot_rating_by_genre(data):
    plt.figure(figsize=(10, 10))  # 調整圖表尺寸
    data.boxplot(column='rating', by='genre', grid=False)
    plt.title('Rating by Genre', fontsize=24)  # 調整標題字體
    plt.xlabel('Genre', fontsize=10)  # 調整 X 軸標籤字體
    plt.ylabel('Rating', fontsize=10)  # 調整 Y 軸標籤字體
    plt.yticks(fontsize=16)  # 調整 Y 軸刻度字體

    save_path = os.path.join('visualizations', 'rating_by_genre.png')
    return save_plot_to_base64(save_path)



def save_plot_to_base64(save_path=None):
    # 將圖表保存到 memory 中
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    
    plt.close()
    return f"data:image/png;base64,{image_base64}"
