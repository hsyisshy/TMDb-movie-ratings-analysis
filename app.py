import sys
sys.path.append('scripts')
import scrape_tmdb
from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 網站首頁，顯示表單讓使用者輸入要抓取的頁數
@app.route('/')
def index():
    return render_template('index.html')

# 處理表單提交並抓取數據
@app.route('/fetch', methods=['POST'])
def fetch_data():
    pages = request.form.get('pages')
    try:
        pages = int(pages)
        if pages <= 0:
            flash("頁數必須大於 0", "error")
            return redirect(url_for('index'))
        
        # 調用抓取數據的功能
        scrape_tmdb.fetch_and_save_data(pages)
        flash("資料抓取成功！", "success")
        return redirect(url_for('index'))
    except ValueError:
        flash("請輸入有效的整數頁數", "error")
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"抓取資料時發生錯誤: {e}", "error")
        return redirect(url_for('index'))

# 顯示抓取後的結果（你可以進一步擴展此功能來顯示具體數據）
@app.route('/results')
def results():
    if os.path.exists('data/tmdb_popular_movies.csv'):
        data = pd.read_csv('data/tmdb_popular_movies.csv')
        return data.to_html()
    else:
        flash("尚未抓取任何資料", "error")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

