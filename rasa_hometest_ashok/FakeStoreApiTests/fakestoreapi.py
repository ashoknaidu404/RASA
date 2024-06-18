import requests
import pytest
# base url declaration
from requests.exceptions import RequestException
import fakestoreapi
base_url = "https://fakestoreapi.com"

"""creating curd operations """


def get_request(endpoint):
    url = f"{base_url}/{endpoint}"
    response = requests.get(url)
    return response


def post_request(endpoint, data):
    url = f"{base_url}/{endpoint}"
    print("post "+url)
    response = requests.post(url, json=data)
    return response


def put_request(endpoint, data):
    url = f"{base_url}/{endpoint}"
    response = requests.put(url, json=data)
    return response


def delete_request(endpoint):
    url = f"{base_url}/{endpoint}"
    print("Delete"+url)
    response = requests.delete(url)
    return response
