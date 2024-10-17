import pickle
import streamlit as st
import requests

# Replace with your actual OMDb API key
OMDB_API_KEY = "f8b48cc2"

def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    poster_url = data.get('Poster')  # Get the poster URL from the response
    if poster_url != "N/A":
        return poster_url
    else:
        return "https://via.placeholder.com/200x300.png?text=Movie+Poster"  # Placeholder if no poster is available

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movies.iloc[i[0]].title))  # Fetch poster using the OMDb API

    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.image(recommended_movie_posters[0])  # Display poster first
        st.text(recommended_movie_names[0])      # Display title below
    with col2:
        st.image(recommended_movie_posters[1])  # Display poster first
        st.text(recommended_movie_names[1])      # Display title below
    with col3:
        st.image(recommended_movie_posters[2])  # Display poster first
        st.text(recommended_movie_names[2])      # Display title below
    with col4:
        st.image(recommended_movie_posters[3])  # Display poster first
        st.text(recommended_movie_names[3])      # Display title below
    with col5:
        st.image(recommended_movie_posters[4])  # Display poster first
        st.text(recommended_movie_names[4])      # Display title below