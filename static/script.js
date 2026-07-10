async function getRecommendation() {
    let movie = document.getElementById("movie").value;
    let response = await fetch("/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            movie: movie
        })
    });
    let data = await response.json();
    let result = document.getElementById("result");
    result.innerHTML = "";
    if (data.error) {
        result.innerHTML = "<h3>" + data.error + "</h3>";
        return;
    }
    result.innerHTML = "<h3>Recommended Movies:</h3>";
    let list = "<ul>";
    data.recommendations.forEach(function(movie) {
        list += "<li>" + movie + "</li>";
    });
    list += "</ul>";
    result.innerHTML += list;
}