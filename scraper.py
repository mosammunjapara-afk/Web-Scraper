import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Scrape a website and extract key information
    
    Args:
        url (str): The website URL to scrape
        
    Returns:
        dict: Scraped data including title, headings, paragraphs, and links
    """
    try:
        # Add headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make the request with timeout
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract data
        data = {
            "title": soup.title.string if soup.title else "No title found",
            "headings": [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]) if h.get_text(strip=True)],
            "paragraphs": [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)],
            "links": [a.get("href") for a in soup.find_all("a", href=True)]
        }
        
        return data

    except requests.exceptions.Timeout:
        return {"error": "Request timeout - The website took too long to respond"}
    
    except requests.exceptions.ConnectionError:
        return {"error": "Connection error - Unable to connect to the website"}
    
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error - {str(e)}"}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Request error - {str(e)}"}
    
    except Exception as e:
        return {"error": f"Unexpected error - {str(e)}"}
