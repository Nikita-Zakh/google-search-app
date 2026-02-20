import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

def get_google_results(query):
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        return []

    params = {
        "q": query,
        "engine": "google",
        "api_key": api_key,
        "num": 5,
        "hl": "cs",
        "gl": "cz"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("organic_results", [])