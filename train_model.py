import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv("dataset/movies.csv")
print(movies.head())
movies["genres"] = movies["genres"].fillna("") #Replacing missing values with an empty string
tfidf = TfidfVectorizer(stop_words="english")
genre_matrix = tfidf.fit_transform(movies["genres"]) #Converting genres into numerical vectors
similarity = cosine_similarity(genre_matrix) #Calculating cosine similarity between movies
joblib.dump(similarity, "similarity.pkl") #Saving the similarity matrix
joblib.dump(movies, "movies.pkl") #Saving the movie dataset
print("Model created successfully!")