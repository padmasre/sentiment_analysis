import streamlit as st
from st_functions import st_button, load_css
import pickle
import sklearn


with st.sidebar:
  st_button('linkedin', 'https://www.linkedin.com/in/padmasreers', 'linkedin.com/in/padmasreers', 20)
  st_button('github', 'https://github.com/padmasre/sentiment_analysis', 'github.com/padmasre/sentiment_analysis', 20)

movie_name = st.text_input(
  "Enter the name of the move here",
  placeholder="Enter the movie name.",
  key="moviename"
)

if len(movie_name) > 0:
  reviews = st.text_area(
    "Enter movie reviews below 👇",
    placeholder="Enter one review per line. Example:\n The movie was fun.\nIt was disappointing",
    key="reviews",
  )
