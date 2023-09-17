import streamlit as st
from st_functions import st_button, load_css
import pickle
import pandas as pd


# Get User Input
st.markdown("## Sentiment Analysis of Moview Reviews")
movie_name = st.text_input(
  "Enter the name of the movie 🎥",
  placeholder="Movie name",
  key="moviename"
)
reviews = []
if len(movie_name) > 0:
  reviews = st.text_area(
    "Enter movie reviews ✍️ below 👇",
    placeholder="Enter one review per line. Example: \nThe movie was fun.\nIt was disappointing.",
    key="reviews",
  )

# Predict review sentiment
if len(reviews) > 0:
  model = pickle.load(open(f'model/model.pkl', 'rb'))
  reviews = reviews.split("\n")
  review_predictions = model.predict(reviews).tolist()
  
  positive_reviews = review_predictions.count(1)
  negative_reviews = review_predictions.count(0)
  st.markdown("⭐Results⭐")
  st.write(f"✔️ No of Positive review: {positive_reviews}")
  st.write(f"⭕ No of Negative review: {negative_reviews}")
  chart_data = pd.DataFrame(
      [[movie_name, positive_reviews, 0],[movie_name, 0, negative_reviews]],
      columns=['Movie','Positive', 'Negative'])
  st.bar_chart(
    chart_data,
    y=['Positive', 'Negative'],
    color=['#FF0000','#0000FF'] 
  )
  # for i in review_predictions:
  #   if i == 1:
  #     st.write("This is a positive review")
  #   elif i == 0:
  #     st.write("This is a negative review")
  #   else:
  #     print("None")

##########################################################
# Personal profile links
with st.sidebar:
  st_button('linkedin', 'https://www.linkedin.com/in/padmasree5', 'linkedin.com/in/padmasreers', 20)
  st_button('github', 'https://github.com/padmasre/sentiment_analysis', 'github.com/padmasre/sentiment_analysis', 20)
