#!/usr/bin/python3
""" this is return the result """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ this is return the result """
    global after
    user_agent = {'User-Agent': 'hello cool bishoy'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    pass_after = {'after': after}
    results = requests.get(url, params=pass_after, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")

        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)

        all_titles = results.json().get("data").get("children")

        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
