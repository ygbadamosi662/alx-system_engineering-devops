#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests

def count_words(subreddit, word_list, after='', word_dict=None):
    """ A function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """

    if word_dict is None:
        word_dict = {}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return

    data = response.json().get("data")
    after = data.get("after")

    for child in data.get("children"):
        title = child.get("data").get("title")
        for word in word_list:
            if word.lower() in title.lower().split():
                word_dict[word.lower()] = word_dict.get(word.lower(), 0) + 1

    if after is not None:
        count_words(subreddit, word_list, after, word_dict)

    if after is None:
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print("{}: {}".format(word, count))
