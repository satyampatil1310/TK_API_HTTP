import requests
from datetime import datetime
parameters = {
            "token": "abcdefghijk1123@",
            "username": "patil",
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
USER_NAME = "patil"
response = requests.post("https://pixe.la/v1/users", json=parameters)
graph_parameters = {
        "id": "x1y1z1",
        "name": "habbit tracker",
        "unit": "hours",
        "type": "int",
        "color": "sora",
}

header = {"X-USER-TOKEN": "abcdefghijk1123@",}
graph_endpoints = requests.post(f"https://pixe.la/v1/users/{USER_NAME}/graphs", json=graph_parameters, headers=header)

get_graph = requests.get(f"https://pixe.la/v1/users/{USER_NAME}/graphs", headers=header)

date = datetime.now().strftime("%Y%m%d")
print(type(date))

increment = {"date": date, "quantity": "5"}

add_increment = requests.post(f"https://pixe.la/v1/users/{USER_NAME}/graphs/x1y1z1", headers=header, json=increment, )
print(add_increment.text)