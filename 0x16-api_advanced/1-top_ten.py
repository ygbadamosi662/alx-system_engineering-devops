#!/usr/bin/python3
"""lists top_ten function"""
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    param = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=param,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for c in results.get("children"):
        print(c.get("data").get("title"))
