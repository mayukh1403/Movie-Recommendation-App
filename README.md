# Movie Recommendation App

This is a content-based movie recommender system built using Python and Streamlit. It suggests movies similar to a user-provided title by analyzing metadata such as genre, keywords, cast, director, and tagline using TF-IDF and cosine similarity.

## Live App

Access the app here:  
[streamlit link](https://movierecommender-divyeb.streamlit.app)

## Features

- Enter your favorite movie name in a search box.
- The system finds the closest matching movie title from the dataset.
- Top 30 similar movies are recommended based on content similarity.
- Built using a simple and clean Streamlit interface.

## How It Works

1. Missing values in the metadata are filled.
2. Features like genres, keywords, cast, director, and tagline are combined into a single string.
3. The combined text is vectorized using **TF-IDF**.
4. **Cosine similarity** is used to measure how close movies are to each other.
5. The app uses **fuzzy matching** to handle slight spelling errors or typos.

## Dataset

The recommendation system uses a movie metadata file (`movies.csv`) that includes:
- Movie titles
- Genres
- Keywords
- Taglines
- Cast & Directors

This data is used only within the deployed app and is not intended for public reuse.
