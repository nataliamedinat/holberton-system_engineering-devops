#!/usr/bin/python3
""" """
import json
import requests


def number_of_subscribers(subreddit):
    """ Get the number os subscribers of a given subreddit """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {'User-Agent': 'My User Agent 1.0'}

    request = requests.get(url, headers=headers)
    req = request.json()

    if request.status_code == 404:
        return 0

    subs = req.get('data').get('subscribers')
    return subs
