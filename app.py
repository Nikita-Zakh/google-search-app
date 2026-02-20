from flask import Flask, render_template, request, jsonify
from services.google_service import get_google_results

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    if request.method == "POST":
        query = request.form.get("query", "")
        results = get_google_results(query)
    return render_template("index.html", query=query, results=results)

@app.route("/download")
def download():
    query = request.args.get("query", "")
    results = get_google_results(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)