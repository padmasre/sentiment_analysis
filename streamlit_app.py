import streamlit as st
from st_functions import st_button, load_css
import pickle
import sklearn


# Get User Input
movie_name = st.text_input(
  "Enter the name of the move here",
  placeholder="Enter the movie name.",
  key="moviename"
)
if len(movie_name) > 0:
  reviews = st.text_area(
    "Enter movie reviews below 👇",
    placeholder="Enter one review per line. Example: \nThe movie was fun.\nIt was disappointing.\nThe movie had great VFX",
    key="reviews",
  )

# Predict review sentiment
if len(reviews) > 0:
  model = pickle.load(open(f'{path}/model/model.pkl', 'rb'))
  reviews_df = pd.DataFrame(reviews)
  reviews_series = reviews_df.iloc[0,:]
  predictions = model.predict(reviews_series).tolist()
  for i in predictions:
    if i == 1:
      st.write("This is a positive review")
    elif i == 0:
      st.write("This is a negative review")
    else:
      print("None")

##########################################################
# Personal profile links
with st.sidebar:
  st_button('linkedin', 'https://www.linkedin.com/in/padmasreers', 'linkedin.com/in/padmasreers', 20)
  st_button('github', 'https://github.com/padmasre/sentiment_analysis', 'github.com/padmasre/sentiment_analysis', 20)
