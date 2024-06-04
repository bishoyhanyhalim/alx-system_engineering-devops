#!/usr/bin/python3
""" this is return number of subscribers """

from requests import get


def top_ten(subreddit):
    """func for numbers pass"""

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Hello Bishoy Hany'}

    top_ten_title = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=top_ten_title)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for num in my_data:
            print(num.get('data').get('title'))

    except Exception:
        print("None")
