# -*- coding: utf-8 -*-
import requests


def get_num_characters(title):
    base_url = "https://pt.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "format": "json",
        "prop": "wikitext",
        "page": title
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    page_content = data["parse"]["wikitext"]['*']

    character_count = len(page_content)
    return character_count


if __name__ == "__main__":
    with open('output.txt', 'w') as output:
        output.write('')

    with open('input.txt') as urls:
        urls = urls.readlines()

    i = 1
    n = len(urls)
    for url in urls:
        url = url.replace('\n', '')
        num = get_num_characters(url)

        with open('output.txt', 'a') as output:
            output.write(f'{num}\n')

        print(f'{i}/{n}')
        i += 1
