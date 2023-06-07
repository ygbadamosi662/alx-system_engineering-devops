#!/usr/bin/python3
"""
Get the total number of subscribers
"""

import requests

def number_of_subscribers(subreddit):
    """
    A Python function that queries reddit API to get the total number of subscribers not active userss
    """
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    headers = {'User-Agent': userAgent}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            print("HERE" + data['data']['subscribers'])
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0
number_of_subscribers('this_is_a_fake_subreddit')
