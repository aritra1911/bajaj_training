import requests

def fetch(url: str) -> requests.Response:
    session = requests.Session()
    return session.get(url)
