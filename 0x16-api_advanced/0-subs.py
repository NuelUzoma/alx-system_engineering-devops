#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscibers
(Total subscribers) for a given subreddit. If an invalid subreddit is given
the function should return 0.
"""


import requests


def number_of_subscribers(subreddit):
    """If not a valid subreddit, it should return 0"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            return 0
        else:
            raise
    data = response.json()
    try:
        return data['data']['subscribers']
    except KeyError:
        return 0
