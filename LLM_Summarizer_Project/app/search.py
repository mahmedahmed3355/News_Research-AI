# app/search.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_CSE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")

def search_google(query: str, num_results=5):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": API_KEY,
        "cx": CSE_ID,
        "num": num_results
    }
    response = requests.get(url, params=params)
    results = response.json().get("items", [])
    return [{"title": item["title"], "link": item["link"]} for item in results]

