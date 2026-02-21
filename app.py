from flask import Flask, render_template, request, jsonify
from services.google_service import get_google_results
import os

app = Flask(__name__, template_folder='templates')  # ← КРИТИЧНО!

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    if request.method == "POST":
        query = request.form.get("query", "")
        try:
            results = get_google_results(query)
        except:
            results = []
    return render_template("index.html", query=query, results=results)

@app.route("/download")
def download():
    query = request.args.get("query", "")
    try:
        results = get_google_results(query)
    except:
        results = []
    return jsonify(results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
