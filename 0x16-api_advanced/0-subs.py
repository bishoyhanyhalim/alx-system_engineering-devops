#!/usr/bin/python3
""" this is return number of subscribers """

from requests import get


def number_of_subscribers(subreddit):
    """func for numbers pass"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'hello bishoy'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
