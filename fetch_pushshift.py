import requests

def fetch_pushshift(keyword, size=200):
    url = "https://api.pushshift.io/reddit/search/submission/"
    params = {
        "q": keyword,
        "size": size,
        "sort": "desc"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["data"]
    return []