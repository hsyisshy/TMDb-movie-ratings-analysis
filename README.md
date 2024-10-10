# TMDb Movie Ratings Analysis

This project is a web application that fetches and analyzes popular movie data from The Movie Database (TMDb) API. It allows users to fetch movie ratings, analyze them by genre, and display visualizations such as rating distributions and genre-based comparisons.

## Features

- Fetches popular movie data using TMDb API.
- Saves the fetched data to a CSV file for analysis.
- Provides visualizations of rating distributions, average ratings by genre, and box plots of ratings by genre.
- Built using Flask for the web interface, with Python handling the data scraping, analysis, and visualization.

## Prerequisites

To run this project locally, you will need the following:

- Python 3.x
- A free API key from TMDb: [TMDb API Documentation](https://developers.themoviedb.org/3/getting-started/introduction)
- Flask and other dependencies listed in `requirements.txt`

## Setup and Installation

Follow these steps to set up and run the project on your local machine:

1. **Clone the repository**:
   ```
   git clone https://github.com/hsyisshy/TMDbmovie-ratings-analysis.git
   cd TMDbmovie-ratings-analysis
   ```
2. **Clone the repository**:
Install dependencies: Install the required Python packages using pip:
   ```
    pip install -r requirements.txt
   ```

3. **Clone the repository**:
Create a .env file in the project root and add your TMDb API key:
   ```
    TMDB_API_KEY=your_tmdb_api_key
   ```

4. **Run the application**:
You can run the Flask app locally using the following command:
   ```
    python app.py
   ```

5. **Access the application**: 
Open your web browser and go to http://127.0.0.1:5001 to access the app.


## Project Structure
Here's an overview of the project structure:

```
/TMDbmovie-ratings-analysis/
├── data/                      # Directory to store fetched movie data (CSV)
│   └── tmdb_popular_movies.csv
├── scripts/
│   ├── scrape_tmdb.py          # Script to fetch data from TMDb API
│   └── visualize.py            # Script to generate visualizations
├── templates/
│   ├── index.html              # HTML template for the app interface
│   └── view_data_table.html     # HTML template for viewing fetched data
├── visualizations/             # Directory to store generated visualizations (PNG)
│   ├── genre_avg_rating.png
│   ├── rating_by_genre.png
│   └── rating_distribution.png
├── .env                        # Environment variable file (not included in version control)
├── .gitignore                  # Files and directories to be ignored by Git
├── app.py                      # Main Flask app file
├── README.md                   # Project documentation
```

## How to Use
1. Fetch Movie Data:
- Enter the number of pages you want to fetch (each page contains 20 movies) in the web interface and click "Start Fetching Data."
- The data will be saved to data/tmdb_popular_movies.csv for further analysis.
View Fetched Data:
- Click on the "View Fetched Data" button to view the raw movie data you've retrieved from the TMDb API.

2. Visualize Data:
- Select one of the chart types (Rating Distribution, Average Rating by Genre, or Rating by Genre Box Plot) from the dropdown menu and click "Show Chart" to display the visualization.
- The charts will be saved to the visualizations/ directory.

## Scripts
- scrape_tmdb.py: Contains the logic for fetching data from the TMDb API.
- visualize.py: Handles the generation of various plots (histograms, bar charts, box plots) for visualizing the fetched movie data.

## Visualizations
The app provides the following visualizations:

- Rating Distribution Histogram: Shows the distribution of movie ratings.
- Average Rating by Genre (Bar Chart): Displays the average rating for each movie genre.
- Rating by Genre Box Plot: Compares the rating distribution for each genre.

## Contributing
Contributions are welcome! If you'd like to contribute to the project, feel free to submit a pull request.

## License
This project is licensed under the MIT License.
