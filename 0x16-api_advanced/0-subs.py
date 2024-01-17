#!/usr/bin/python3
"""
ubs module
"""


import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: The number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if 'error' in data or 'subreddit' not in data:
            return 0  # Invalid subreddit or error in response

        subscribers = data['subreddit']['subscribers']
        return subscribers

    except requests.RequestException as e:
        print(f"Error making request: {e}")
        return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))
