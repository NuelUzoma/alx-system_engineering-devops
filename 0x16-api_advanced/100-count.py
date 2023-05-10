#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parse all the title of all
hot articles and prints a sorted count of given keywords
(case insensitive, delimited by spaces)
"""


import requests


def count_words(subreddit, word_list):
    """The recursive function that queries the Reddit API"""
    count_dict = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            return
        else:
            raise
    data = response.json()
    indexes = data['data']['children']
    for index in indexes:
        title = index['data']['children'].lower()
        for word in word_list:
            if word.lower() in title and not title.startswith(word.lower() + '.') and not title.startswith(word.lower() + '!') and not title.startswith(word.lower() + '_'):
                if word.lower() in count_dict:
                    count_dict[word.lower()] += 1
                else:
                    count_dict[word.lower()] = 1
    if len(indexes) == 0:
        return count_dict
    else:
        after = data["data"]["after"]
        if after is not None:
            return count_words(subreddit, word_list, count_dict=count_dict)
        else:
            sorted_counts = sorted(count_dict.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return count_dict