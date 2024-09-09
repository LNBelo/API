# -*- coding: utf-8 -*-

"""
    Similar to null edit
    Use forcelinkupdate parameter
"""

import requests


def api_request(lst, project="commons"):
    """
    :param lst: list with pages
    :param project: wikimedia project
    :return: force link update
    """

    projects = {
        "commons": "https://commons.wikimedia.org/w/api.php",
        "wikipedia": "https://pt.wikipedia.org/w/api.php"
    }
    base_url = projects[project]
    params = {
        "action": "purge",
        "format": "json",
        "forcelinkupdate": 1,
        "forcerecursivelinkupdate": 1,
        "titles": "|".join(lst),
        "formatversion": "2"
    }

    requests.post(base_url, params=params, headers={'Content-Type': 'application/json'})


with open("input.txt", encoding='utf-8') as lines:
    lines = lines.readlines()

len_items = len(lines)
total = len_items // 50
first = 0
last = 50

for i in range(total + 1):
    pages = lines[first:last]
    pages = [page.strip() for page in pages]

    if len(pages) > 0:
        api_request(pages)

        if i != total:
            print(f"{last}/{len_items}")
        else:
            print(f"{len_items}/{len_items}")

        first += 50
        last += 50
