# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from new_egg_scraper import new_egg_scrape  # <- your existing function

app = Flask(__name__)
CORS(app)  # allow requests from your React dev server

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.get_json() or {}
    url = data.get("url")
    if not url:
        return jsonify({"error": "no url provided"}), 400

    elif 'newegg' in url:
        specs = new_egg_scrape(url)
        print(f"\n=== Scrape result for: {url} ===\n{specs}\n")  # printed to terminal
        return jsonify({"specs": specs}), 200
    else: 
        return jsonify({"error": "Invalid"}), 200
    

if __name__ == "__main__":
    app.run(debug=True)