import requests


def returnResult(query):
    url = "https://api.sumanjay.cf/torrent/?query={}".format(update.message.text)
    result = requests.get(url)
    return result.json()['results']
