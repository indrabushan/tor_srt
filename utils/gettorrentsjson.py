import requests, config


def returnResult(query):
    result = requests.get(
        f'{config.apiUrl}{query}')
    return result.json()['results']
