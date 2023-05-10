#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first
10 hot spots listed for a subreddit. Invalid subreddits may return a redirect
to search results. Ensure there are no redirects.
"""


import requests


def top_ten(subreddit):
    """Returns the titles of the first 10 hot spots"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            print(None)
            return
        else:
            raise
    data = response.json()
    for post in data['data']['children'][:10]:
        print(post['data']['title'])
