import streamlit as st
from st_functions import st_button, load_css

st.write('Hi!')

with st.sidebar:
  st_button('linkedin', 'https://www.linkedin.com/in/padmasreers', 'linkedin.com/in/padmasreers', 20)
