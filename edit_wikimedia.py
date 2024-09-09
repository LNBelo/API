import requests
from API import user_config


def edit(title, text, project="test"):
    S = requests.Session()

    projects = {
        "test": "https://test.wikipedia.org/w/api.php",
        "commons": "https://commons.wikimedia.org/w/api.php",
        "wikisource": "https://pt.wikisource.org/w/api.php"
    }
    URL = projects[project]

    # Step 1: GET request to fetch login token
    PARAMS_0 = {
        "action": "query",
        "meta": "tokens",
        "type": "login",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS_0)
    DATA = R.json()

    LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

    # Step 2: POST request to log in. Use of main account for login is not
    PARAMS_1 = {
        "action": "login",
        "lgname": user_config.username,
        "lgpassword": user_config.password,
        "lgtoken": LOGIN_TOKEN,
        "format": "json"
    }

    R = S.post(URL, data=PARAMS_1)
    DATA = R.json()

    # Step 3: GET request to fetch CSRF token
    PARAMS_2 = {
        "action": "query",
        "meta": "tokens",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS_2)
    DATA = R.json()

    CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

    # Step 4: POST request to edit a page
    PARAMS_3 = {
        "action": "edit",
        "title": title,
        "token": CSRF_TOKEN,
        "text": text,
        "format": "json"
    }

    R = S.post(URL, data=PARAMS_3)
    return R.json()

