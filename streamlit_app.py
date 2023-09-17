import streamlit as st
from st_functions import st_button, load_css

st.write('Hi!')

text_input = st.text_input(
  "Enter your movie review below 👇",
  "The movie was fun to watch with family",
  key="userinput",
)

if text_input:
    st.write("You wrote: ", text_input)
