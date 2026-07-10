from flask import Flask, render_template, request, jsonify
import joblib
from sklearn.metrics.pairwise import cosine_similarity
app = Flask(__name__)
movies = joblib.load("movies.pkl")
genre_matrix = joblib.load("genre_matrix.pkl")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/health")
def health():
    return jsonify({"status": "OK"})
@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()
        if not data or "movie" not in data:
            return jsonify({"error": "Movie name is required"}), 400
        movie_name = data["movie"]
        if movie_name not in movies["title"].values:
            return jsonify({"error": "Movie not found"}), 404
        movie_index = movies[movies["title"] == movie_name].index[0]
        scores = cosine_similarity(
            genre_matrix[movie_index],
            genre_matrix
        ).flatten()
        similarity_scores = list(enumerate(scores))
        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )
        recommendations = []
        for movie in similarity_scores[1:6]:
            recommendations.append(
                movies.iloc[movie[0]]["title"]
            )
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True)