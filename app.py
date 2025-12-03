import streamlit as st
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Movie Recommendation App")

@st.cache_data
def load_data_and_similarity():
    movies_data = pd.read_csv('movies.csv')
    selected_features = ['genres','keywords','tagline','cast','director']

    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')

    combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

    #Feature Extraction
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)

    #Cosine Similarity
    similarity = cosine_similarity(feature_vectors)

    return movies_data, similarity

movies_data, similarity = load_data_and_similarity()

movie_name = st.text_input('Enter your favourite movie name:')

if movie_name:
    title_list = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, title_list)

    if find_close_match:
        close_match = find_close_match[0]
        st.success(f"Showing results for: {close_match}")

        index_of_movie = movies_data[movies_data['title'] == close_match].index[0]

        similarity_score = list(enumerate(similarity[index_of_movie]))
        sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

        st.subheader("Top 30 Recommended Movies:")
        for i, movie in enumerate(sorted_similar_movies[1:31], start=1):
            index = movie[0]
            title_from_index = movies_data.iloc[index]['title']
            st.write(f"{i}.{title_from_index}")
    else:
        st.error("No close match found in dataset. Try a different title")
