#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
the given subreddit, it should return None.
"""


import requests


def recurse(subreddit, hot_list=[]):
    """The recursive function that will be used to for queries"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            return None
        else:
            raise
    data = response.json()
    indexes = data['data']['children']
    for index in indexes:
        hot_list.append(index['data']['title'])
    if data['data']['after'] is None:
        return hot_list
    else:
        params['after'] = data['data']['after']
        return recurse(subreddit, hot_list)
