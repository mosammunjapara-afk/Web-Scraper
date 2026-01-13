import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        data = {
            "title": soup.title.string if soup.title else "No title",
            "headings": [h.get_text(strip=True) for h in soup.find_all(["h1","h2","h3","h4","h5","h6"])],
            "paragraphs": [p.get_text(strip=True) for p in soup.find_all("p")],
            "links": [a.get("href") for a in soup.find_all("a", href=True)]
        }
        return data

    except Exception as e:
        return {"error": str(e)}
