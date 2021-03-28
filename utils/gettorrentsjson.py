import requests


def returnResult(query):
    url = "https://api.sumanjay.cf/torrent/?query={}"
    result = requests.get(url).json()
    return result.json()['results']
