# TMDb Movie Ratings Analysis

This project allows users to scrape popular movie data from the TMDb API, analyze ratings, and visualize the results. The project is built using Flask for the web interface and `gunicorn` for local server management.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Key Setup](#api-key-setup)
- [Running the Application](#running-the-application)
- [Features](#features)
- [License](#license)

## Installation

### 1. Clone the repository
To get started, clone the repository from GitHub:
```bash
git clone https://github.com/hsyisshy/TMDb-movie-ratings-analysis.git
cd TMDb-movie-ratings-analysis
```

### 2. Create a virtual environment (Optional but recommended)
To keep dependencies isolated, it is recommended to create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Features
- Movie Scraping: Fetches popular movies from the TMDb API based on the number of pages specified.
- CSV Export: Saves the fetched data as a CSV file for future analysis.
- Web Interface: A simple Flask-based web interface to interact with the TMDb API.
- Genre Analysis: Analyze movie ratings by genre with basic statistics.
- Visualization: Visualize movie rating distributions (can be further expanded).

## License
This project is licensed under the MIT License.
