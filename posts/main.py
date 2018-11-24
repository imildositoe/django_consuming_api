# import requests
# import json
#
# # if __name__ == '__main__':
# #     url = 'http://127.0.0.1:8080/dawapi'
# #     response = requests.get(url)
# #
# #     print(response)
#
# if __name__ == '__main__':
#     url = 'http://127.0.0.1:8080/dawapi/usuario/login'
#     payload = {
#         'usuario': 'grupo',
#         'senha': 'primeiro'
#     }
#     headers = {
#         'Content-type': 'application/json',
#         'Accept': 'application/json'}
#     response = requests.post(url, data=json.dumps(payload), headers=headers)
#     # print(response.text)
#
#     url2 = 'http://127.0.0.1:8080/dawapi/usuario/1'
#     headers2 = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json',
#         'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJub21lIjoiR3J1cG8gUHJpbWVpcm8iLCJpZCI6IjEiLCJleHAiOjE1NDMxNDk5Mzl9.VFLM57XG7HeUx2YW9n63rRVqI6DY9lhplyY6IxsUhRjrtepjcnhyG3zCLHUlTiL3POA-UbvHKKNLwayQxZMrmw'
#     }
#     response2 = requests.get(url, headers=headers2)
#
#     print(response2.content)

import requests
import json

header = {
    "Content-Type": "application/json",
    "Accept": "application/json"

}
data = {'usuario': 'grupo', 'senha': 'primeiro'}
r = requests.post('http://localhost:8080/dawapi/usuario/login', data=json.dumps(data), headers=header)
print(r.status_code)


header1 = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJub21lIjoiR3J1cG8gUHJpbWVpcm8iLCJpZCI6IjEiLCJleHAiOjE1NDMxNTA4NzR9.eXxUfuvgsXOMDJONJl9djJKVR326Zl6Hmh8E3fca7PQfDTqkG0Ol1zlNTWRutzq9Ob_MLVnDgbEXB6KE4cbQEg"

}
r1 = requests.get('http://localhost:8080/dawapi/usuario', headers=header1)
# print(r1.json())

header2 = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJub21lIjoiR3J1cG8gUHJpbWVpcm8iLCJpZCI6IjEiLCJleHAiOjE1NDMxNTA4NzR9.eXxUfuvgsXOMDJONJl9djJKVR326Zl6Hmh8E3fca7PQfDTqkG0Ol1zlNTWRutzq9Ob_MLVnDgbEXB6KE4cbQEg"

}
r2 = requests.get('http://localhost:8080/dawapi/usuario/1', headers=header2)
# print(r2.json())
