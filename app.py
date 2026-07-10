from flask import Flask, render_template, request, jsonify
import joblib
app = Flask(__name__)
movies = joblib.load("movies.pkl")
similarity = joblib.load("similarity.pkl")
@app.route("/") #Home page
def home():
    return render_template("index.html")
@app.route("/health") #Health check API
def health():
    return jsonify({"status": "OK"})
@app.route("/recommend", methods=["POST"]) #Recommendation API
def recommend():
    try:
        data = request.get_json()
        if not data or "movie" not in data:
            return jsonify({"error": "Movie name is required"}), 400
        movie_name = data["movie"]
        if movie_name not in movies["title"].values:
            return jsonify({"error": "Movie not found"}), 404
        movie_index = movies[movies["title"] == movie_name].index[0]
        similarity_scores = list(enumerate(similarity[movie_index]))
        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )
        recommendations = []
        for i in similarity_scores[1:6]:
            recommendations.append(movies.iloc[i[0]]["title"])
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__": #Running the application
    app.run(debug=True)