#!/usr/bin/python3
"""
Function that queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit. If no results are
found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})

    for child in data.get('children', []):
        hot_list.append(child['data']['title'])

    after = data.get('after', None)
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return "OK" if hot_list else None
