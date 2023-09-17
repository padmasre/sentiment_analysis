import streamlit as st
from st_functions import st_button, load_css
import pickle
import pandas as pd


# Get User Input
movie_name = st.text_input(
  "Enter the name of the movie 🎥",
  placeholder="Movie name",
  key="moviename"
)
reviews = []
if len(movie_name) > 0:
  reviews = st.text_area(
    "Enter movie reviews ✍️ below 👇",
    placeholder="Enter one review per line. Example: \nThe movie was fun.\nIt was disappointing.\nThe movie had great VFX",
    key="reviews",
  )

# Predict review sentiment
if len(reviews) > 0:
  model = pickle.load(open(f'model/model.pkl', 'rb'))
  reviews = reviews.split("\n")
  reviews_df = pd.DataFrame(reviews)
  reviews_series = reviews_df.squeeze() # Converting dataframe to series
  review_predictions = model.predict(reviews_series).tolist()
  
  positive_reviews = review_predictions.count(1)
  negative_reviews = review_predictions.count(0)
  total_review = len(reviews)
  st.write("No of Positive and Negative reviews")
  chart_data = pd.DataFrame(
      [[positive_reviews, 0],[negative_reviews, 0]],
      columns=['Positive', 'Negative'])
  st.bar_chart(
    chart_data,
    y=['Positive', 'Negative'],
  )
  for i in review_predictions:
    if i == 1:
      st.write("This is a positive review")
    elif i == 0:
      st.write("This is a negative review")
    else:
      print("None")

##########################################################
# Personal profile links
with st.sidebar:
  st_button('linkedin', 'https://www.linkedin.com/in/padmasree5', 'linkedin.com/in/padmasreers', 20)
  st_button('github', 'https://github.com/padmasre/sentiment_analysis', 'github.com/padmasre/sentiment_analysis', 20)
