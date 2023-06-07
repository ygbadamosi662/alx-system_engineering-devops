#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")

    for c in data.get("children"):
        hot_list.append(c.get("data").get("title"))
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)

    if after:
        return recurse(subreddit, hot_list=hot_list, after, count)

    return hot_list
