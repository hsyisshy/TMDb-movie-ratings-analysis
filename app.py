import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# 將 'scripts' 文件夾添加到路徑，以便 import 模組
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
import scrape_tmdb  # 導入我們剛剛創建的爬蟲模組

data = None  # 全局變數存儲數據

# 函數：抓取資料
def fetch_data():
    try:
        pages_input = page_entry.get().strip()
        if not pages_input.isdigit():
            raise ValueError("請輸入有效的整數頁數")
        
        pages = int(pages_input)
        if pages <= 0:
            raise ValueError("頁數必須大於 0")
        
        file_path = scrape_tmdb.fetch_and_save_data(pages)
        global data
        data = pd.read_csv(file_path)
        data['genres'] = data['genres'].str.split(',')
        data = data.explode('genres')
        messagebox.showinfo("成功", "資料抓取完成並保存。")
    
    except ValueError as ve:
        messagebox.showerror("錯誤", f"無效的輸入：{ve}")
    except Exception as e:
        messagebox.showerror("錯誤", f"抓取資料時發生錯誤：{e}")

# 圖表顯示函數
def show_rating_distribution():
    if data is None:
        messagebox.showwarning("資料未加載", "請先抓取資料")
        return
    plt.figure(figsize=(10, 6))
    plt.hist(data['rating'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def show_genre_avg_rating():
    if data is None:
        messagebox.showwarning("資料未加載", "請先抓取資料")
        return
    genre_avg_rating = data.groupby('genres')['rating'].mean().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    genre_avg_rating.plot(kind='bar', color='coral')
    plt.title('Average Movie Ratings by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_rating_distribution_by_genre():
    if data is None:
        messagebox.showwarning("資料未加載", "請先抓取資料")
        return
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='genres', y='rating', data=data, palette='Set3')
    plt.title('Movie Ratings Distribution by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Rating')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 創建主窗口
root = tk.Tk()
root.title("Movie Ratings Analysis")

# 設置窗口大小
root.geometry("400x500")

# 添加標題標籤
label = tk.Label(root, text="Movie Ratings Analysis", font=("Arial", 18))
label.pack(pady=20)

# 添加頁數輸入框
page_label = tk.Label(root, text="請輸入要抓取的頁數：", font=("Arial", 14))
page_label.pack(pady=10)
page_entry = tk.Entry(root, font=("Arial", 14), width=10)
page_entry.pack(pady=10)

# 添加抓取資料按鈕
fetch_button = tk.Button(root, text="抓取資料", command=fetch_data, font=("Arial", 14))
fetch_button.pack(pady=20)

# 添加按鈕來顯示不同的圖表
btn1 = tk.Button(root, text="顯示評分分布圖", command=show_rating_distribution, font=("Arial", 14))
btn1.pack(pady=10)

btn2 = tk.Button(root, text="顯示類型平均評分圖", command=show_genre_avg_rating, font=("Arial", 14))
btn2.pack(pady=10)

btn3 = tk.Button(root, text="顯示評分與類型箱型圖", command=show_rating_distribution_by_genre, font=("Arial", 14))
btn3.pack(pady=10)

# 運行主循環
root.mainloop()
