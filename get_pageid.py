# -*- coding: utf-8 -*-
import re

import requests
import pandas as pd


def get_page_ids(titles):
    endpoint = 'https://pt.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'format': 'json',
        'titles': '|'.join(titles)
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    page_ids = {}
    for page_id, page_info in data['query']['pages'].items():
        title = page_info['title']
        if re.match('-', page_id):
            page_ids[title] = None
        else:
            page_ids[title] = page_id

    return page_ids


def main():
    with open('input.txt', encoding='utf-8') as file:
        titles = [line.strip() for line in file.readlines()]

    all_page_ids = {}
    n = 1
    # Process titles in chunks of 50
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        page_ids = get_page_ids(chunk)
        all_page_ids.update(page_ids)
        print(f"{n} / {len(titles) // 50}")
        n += 1

    # Prepare data for the Excel file
    data = {
        'Title': list(all_page_ids.keys()),
        'Page ID': [all_page_ids[title] for title in all_page_ids]
    }

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False, engine='openpyxl')


if __name__ == "__main__":
    main()
