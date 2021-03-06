import requests
from pprint import pprint


def fetch_models(models_info):
    url = "https://o9upvhes.api.sanity.io/v1/data/query/production?query=*%5B_type%3D%3D'kunstigModel'%5D%7B%0A%20%20name%2C%0A%20%20displayName%2C%0A%20%20description%2C%0A%20%20%22url%22%3Amodel.asset-%3Eurl%2C%0A%20%20%22images%22%3Aimages%5B%5D.asset-%3Eurl%0A%7D"
    resp = requests.get(url=url)
    data = resp.json()
    models_info.clear()
    for model in data['result']:
        if 'url' in model:
            models_info[model['name']] = model
