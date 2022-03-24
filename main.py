from pprint import pprint
from time import sleep

import requests

TOKEN = '5f997dcb019ee45d31483b063ca450a9783d9bf15b63e06ae663807d727a5323ba3e62c70f227b1a1ac5c'
# TOKEN = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'
# URL = 'https://api.vk.com/method/users.get'
PARAMS = {
    # 'user_id': '1',
    'access_token': TOKEN,
    'v': 5.131,
    # 'fields': 'education, sex'
}


class user():
    type = 'vk'
    url = 'https://api.vk.com/method/'
    friends = []
    inst = []
    def __init__(self, id):
        self.id = id
        # id =
        print(f'Создал юзера c id = {self.id}')
        # self.type = 'not vk'
        self.friends.append(id)
        self.inst.append(self)
        return

    def getFollowersIDs(self, id=None):
        if id is None:
            id = self.id
        get_fol_url = self.url +  'users.getFollowers'
        followers_params = {'user_id': id}
        data = requests.get(get_fol_url, params={**PARAMS, **followers_params})
        data.raise_for_status()
        data = data.json()
        items = data['response']['items']
        items = sorted(items)
        return items

def getMyID():
    print('Получаю свой ID')
    url = 'https://api.vk.com/method/users.get'
    data = requests.get(url, params=PARAMS).json()
    list_id = data['response']
    id = list_id[0]['id']
    return id


# def search_query(q, sorting=0):
#     url = 'https://api.vk.com/method/groups.search'
#     params = {
#         'q': q,
#         'access_token': TOKEN,
#         'v': 5.131,
#         'sort': sorting,
#         'count': 300
#     }
#     data = requests.get(url, params).json()
#     # pprint(data)
#     data = data["response"]["items"]
#     return data


if __name__ == '__main__':
    my_id = getMyID()
    my_user = user(my_id)
    # print(my_user.id)
    # pprint(my_user.getFollowers().json())
    my_friend_ids = my_user.getFollowersIDs(my_id)
    print(my_friend_ids)
    # print(len(my_friend_ids))
    list_var = [('user' + str(i+1)) for i in range(len(my_friend_ids))]
    print(list_var)
    # user1 = user(my_friend_ids[0])
    # user2 = user(my_friend_ids[1])
    list_all = []
    for i, fr in enumerate(list_var):
        fr = user(my_friend_ids[i])
        list_all.append({"id": fr.id, "followers": fr.getFollowersIDs()})
        # list_all["followers"] = fr.getFollowersIDs()
        print(list_all)
        sleep(0.5)
    for i, user_var in enumerate(list_all):
        for user_fol in user_var["followers"]:
            for j in range(len(list_all)- i - 1):
                if user_fol in list_all[i + j + 1]["followers"]:
                    print(f'Общий друг – {user_fol} у {list_all[i]["id"]} и {list_all[i + j]["id"]}')
    # print()
    # list1 = user1.getFollowersIDs()
    # list2 = user2.getFollowersIDs()
    # for id in list1:
    #     if id in list2:
    #         print(id)
        # else:
            # print(f'{id} нет у {user2.id}')
    print(user.friends)
    print(user.inst)
    # for i, var in enumerate(list_var):
    #     list_fol = var.getFollowersID
    #     for fol in list_fol:
    #         if fol in list_var
    #
    #
    # for var in list_var:
    #     dict_all["id"] = var
    #     dict_all["followers"] = var.getFollowersIDs()
    #     print(dict_all)
