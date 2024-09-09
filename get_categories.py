# -*- coding: utf-8 -*-
import requests


def get_categories(title):
    base_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "categories",
        "titles": title
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    pages = data["query"]["pages"]

    payload = []
    for page_id, page_info in pages.items():
        categories = page_info.get('categories', [])
        for category in categories:
            payload.append(category['title'])

    return payload


if __name__ == "__main__":
    with open('output.txt', 'w') as output:
        output.write('')

    with open('input.txt') as pages:
        pages = pages.readlines()

    i = 1
    n = len(pages)
    for page in pages:
        page = page.replace('\n', '')
        cat = get_categories(page)

        with open('output.txt', 'a') as output:
            output.write(f'{cat}\n')

        print(f'{i}/{n}')
        i += 1
