import streamlit as st
from st_functions import st_button, load_css
import pickle
import sklearn


with st.sidebar:
  st_button('linkedin', 'https://www.linkedin.com/in/padmasreers', 'linkedin.com/in/padmasreers', 20)
  st_button('github', 'https://github.com/padmasre/sentiment_analysis', 'github.com/padmasre/sentiment_analysis', 20)

text_input = st.text_input(
  "Enter your movie review below 👇",
  placeholder="The movie was fun to watch with family",
  key="userinput",
)

if text_input:
    st.write("You wrote: ", text_input)
