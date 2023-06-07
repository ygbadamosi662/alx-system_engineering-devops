#!/usr/bin/python3
"""
Get the total number of subscribers
"""


from requests import get


def number_of_subscribers(subreddit):
    """
    A Python function that queries reddit API to get the total number of subscribers not active userss
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Microsoft Edge Version 113.0.1774.57'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
