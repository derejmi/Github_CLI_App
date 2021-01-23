import requests

from .repo import Repo



def fetch_repos(username):
    URL = f'https://api.github.com/users/{username}/repos'
    '''Call to Github API '''

    resp = requests.get(URL)
    print(resp.json(), "Response Json")
    for data in resp.json():
        Repo(data)
        

