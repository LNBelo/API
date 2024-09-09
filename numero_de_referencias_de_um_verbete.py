import requests
from bs4 import BeautifulSoup


def cont_ref(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    reference_elements = soup.find_all('sup', {'class': 'reference'})
    return len(reference_elements)


with open('output.txt', 'w') as output:
    output.write('')

with open('input.txt') as urls:
    urls = urls.readlines()

i = 1
n = len(urls)
for url in urls:
    url = url.replace('\n', '')
    num = cont_ref(url)

    with open('output.txt', 'a') as output:
        output.write(f'{num}\n')

    print(f'{i}/{n}')
    i += 1
