import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
movies = pd.read_csv("dataset/movies.csv")
movies["genres"] = movies["genres"].fillna("")
tfidf = TfidfVectorizer(stop_words="english")
genre_matrix = tfidf.fit_transform(movies["genres"])
joblib.dump(movies, "movies.pkl")
joblib.dump(tfidf, "vectorizer.pkl")
joblib.dump(genre_matrix, "genre_matrix.pkl")
print("Model created successfully!")