"""Free API Checker — test if APIs are working and measure response times."""
import json
import time
import urllib.request
from dataclasses import dataclass

@dataclass
class APIEndpoint:
    name: str
    url: str
    auth_required: bool = False
    description: str = ""

FREE_APIS = [
    APIEndpoint("JSONPlaceholder", "https://jsonplaceholder.typicode.com/posts/1", False, "Fake REST API for testing"),
    APIEndpoint("httpbin", "https://httpbin.org/get", False, "HTTP request testing"),
    APIEndpoint("Dog API", "https://dog.ceo/api/breeds/image/random", False, "Random dog images"),
    APIEndpoint("Cat Facts", "https://catfact.ninja/fact", False, "Random cat facts"),
    APIEndpoint("GitHub API", "https://api.github.com", False, "GitHub public API"),
    APIEndpoint("Open Meteo", "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true", False, "Weather data"),
    APIEndpoint("IP API", "https://ipapi.co/json/", False, "IP geolocation"),
    APIEndpoint("Wikipedia", "https://en.wikipedia.org/api/rest_v1/page/random/summary", False, "Random Wikipedia article"),
    APIEndpoint("arXiv", "https://export.arxiv.org/api/query?search_query=all:ai&max_results=1", False, "Academic papers"),
    APIEndpoint("PubMed", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=cancer&retmode=json&retmax=1", False, "Medical papers"),
]

def check_api(endpoint: APIEndpoint, timeout: int = 10) -> dict:
    """Check if an API endpoint is working."""
    start = time.time()
    try:
        req = urllib.request.Request(endpoint.url, headers={"User-Agent": "APIChecker/1.0"})
        resp = urllib.request.urlopen(req, timeout=timeout)
        latency = (time.time() - start) * 1000
        return {"name": endpoint.name, "status": "UP", "latency_ms": round(latency), "code": resp.status}
    except Exception as e:
        return {"name": endpoint.name, "status": "DOWN", "error": str(e)[:50]}

def check_all() -> list[dict]:
    """Check all free APIs and return results."""
    results = []
    for api in FREE_APIS:
        result = check_api(api)
        status_icon = "✓" if result["status"] == "UP" else "✗"
        latency = f"{result.get('latency_ms', 0)}ms" if result["status"] == "UP" else result.get("error", "")
        print(f"  {status_icon} {api.name:<20} {result['status']:<6} {latency}")
        results.append(result)
    return results

if __name__ == "__main__":
    print("Checking 10 free APIs...\n")
    results = check_all()
    up = sum(1 for r in results if r["status"] == "UP")
    print(f"\n{up}/{len(results)} APIs working")
