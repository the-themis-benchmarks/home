import json

import requests


def get_phone_name(index):
    if index < 10:
        return "cph-v9xc-1-0000" + str(index)
    return "cph-v9xc-1-000" + str(index)


def get_phones():
    url = "https://cph.cn-south-1.myhuaweicloud.com/v1/0a82da3dec00f43a2f45c004d252ae44/cloud-phone/phones"
    params = {
        "server_id": "1106f4edf47c4e8f9130a021f67dc447",
    }
    headers = {
        "X-Auth-Token": get_token()
    }
    phone_list_res = requests.get(url=url, params=params, headers=headers)
    phone_list = json.loads(phone_list_res.text)["phones"]
    phone_map = {}
    for phone in phone_list:
        phone_map[phone["phone_name"]] = phone["phone_id"]
    return phone_map


def reset_phone(phone_id):
    url = "https://cph.cn-south-1.myhuaweicloud.com/v1/0a82da3dec00f43a2f45c004d252ae44/cloud-phone/phones/batch-reset"
    params = {
        "phones": [
            {
                "phone_id": phone_id
            }
        ]
    }
    headers = {
        "X-Auth-Token": get_token()
    }

    r = requests.post(url=url, data=json.dumps(params), headers=headers)
    print(r.text)
    print("=============================================")


def phone_reset_finish(phone_id):
    url = "https://cph.cn-south-1.myhuaweicloud.com/v1/0a82da3dec00f43a2f45c004d252ae44/cloud-phone/phones/" + phone_id
    headers = {
        "X-Auth-Token": get_token()
    }
    phone_state_res = requests.get(url=url, headers=headers)
    phone_state = json.loads(phone_state_res.text)
    return phone_state["status"] == 2


def get_token():
    url = "https://iam.cn-south-1.myhuaweicloud.com/v3/auth/tokens"
    data = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": "hw_008613632826027_01",
                        "password": "Zz102938",
                        "domain": {
                            "name": "hw_008613632826027_01"
                        }
                    }
                }
            },
            "scope": {
                "project": {
                    "name": "cn-south-1"
                }
            }
        }
    }
    headers = {
        "Content-Type": "application/json",

    }
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    return r.headers.get("X-Subject-Token")


if __name__ == '__main__':
    print(get_token())
    # print("================================================")
    # print(get_phones())
    # print("================================================")
    # # reset_phone("300295ccf4c94c67879069eb35527756")
    # print(phone_reset_finish("300295ccf4c94c67879069eb35527756"))
