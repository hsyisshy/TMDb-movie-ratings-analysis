import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, Response
from scripts.scrape_tmdb import fetch_data_from_api
from scripts.visualize import plot_rating_distribution, plot_genre_avg_rating, plot_rating_by_genre


app = Flask(__name__)
app.secret_key = 'your_secret_key' 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    pages = int(request.form.get('pages'))
    data = fetch_data_from_api(pages)
    data.to_csv('data/tmdb_popular_movies.csv', index=False)
    flash(f'successfully! A total of {pages} pages were fetched.', 'success')
    return render_template('index.html')

@app.route('/visualize_data', methods=['POST'])
def visualize_data():
    chart_type = request.form.get('chart_type')
    data = pd.read_csv('data/tmdb_popular_movies.csv')

    if chart_type == 'rating_distribution':
        plot_url = plot_rating_distribution(data)
    elif chart_type == 'genre_avg_rating':
        plot_url = plot_genre_avg_rating(data)
    elif chart_type == 'rating_by_genre':
        plot_url = plot_rating_by_genre(data)
    else:
        plot_url = None

    return render_template('index.html', plot_url=plot_url)

@app.route('/view_data', methods=['GET'])
def view_data():
    data = pd.read_csv('data/tmdb_popular_movies.csv')
    table_html = data.to_html(classes='table table-bordered table-striped', index=False)
    return render_template('view_data_table.html', table_html=table_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001, debug=True)

