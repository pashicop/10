from pprint import pprint

import requests
TOKEN = '5f997dcb019ee45d31483b063ca450a9783d9bf15b63e06ae663807d727a5323ba3e62c70f227b1a1ac5c'
URL = 'https://api.vk.com/method/users.get'
PARAMS = {
    'user_id': '1',
    'access_token': TOKEN,
    'v': 5.131,
    'fields': 'education, sex'
}

def search_query(q, sorting=0):
    url = 'https://api.vk.com/method/groups.search'
    params = {
        'q': q,
        'access_token': TOKEN,
        'v': 5.131,
        'sort': sorting,
        'count': 300
    }
    data = requests.get(url, params).json()
    # pprint(data)
    data = data["response"]["items"]
    return data
if __name__ == '__main__':
    # response = requests.get(URL, params=PARAMS)
    # response.raise_for_status()
    # data = response.json()
    # pprint(data)
    list = search_query('python')
    print(len(list))
    for group in list:
        print(group['id'])
