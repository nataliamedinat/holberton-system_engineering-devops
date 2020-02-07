#!/usr/bin/python3
""" Top ten """

import json
import requests


def top_ten(subreddit):
    """ Print the tittles of the first 10 hot posts """

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    request = requests.get(url, headers=headers)
    req = request.json()

    if request.status_code == 404:
        print(None)

    else:
        hot = req.get('data').get('children')
        for count in hot:
            print(count.get('data').get('title'))
