from flask import Flask, render_template, request, send_file
from scraper import scrape_website
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.form["url"]
    data = scrape_website(url)

    # Save result to a JSON file
    file_path = "scraped_data.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return render_template("result.html", data=data, url=url)

@app.route("/download")
def download():
    return send_file("scraped_data.json", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
