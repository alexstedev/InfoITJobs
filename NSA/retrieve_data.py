import requests
import pandas as pd

payload = {}
headers = {
    'Authorization': 'Basic MWVlZDc3ZDJjZTJjNDQwMThiYWRjM2U0MGJkOTY1Y2E6RFBqYzdkMVNjNUlsRzRGTXZNVlFwaFA    4S2tXdkU2d0lnU3FYOW5rZ1Z0S2JaTkVzK1o=',
    'Cookie': 'IJUSERUID=3b364be8-a072-47b8-bac4-34f29903ceb4; JSESSIONID=TJpfc6KysyOynUJQl3roTCKE'
}


url = "https://api.infojobs.net/api/7/offer?category=informatica-telecomunicaciones&maxResults=100"
response = requests.request("GET", url, headers=headers, data=payload)
data_2 = response.json() if response and response.status_code == 200 else None

# DICT sc-id to sc-str
sc_id_to_name = {}
for i in range(len(data_2['items'])):
    sc_id_to_name[data_2['items'][i]['subcategory']['id']
                  ] = data_2['items'][i]['subcategory']['value']

url = "https://api.infojobs.net/api/1/candidate/skillcategory"
response = requests.request("GET", url, headers=headers, data=payload)
data_1 = response.json() if response and response.status_code == 200 else None


def jobs_from_sc(sc_name: str):  # given sc id
    url = "https://api.infojobs.net/api/7/offer?subcategory="+sc_name+"&maxResults=100"
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json() if response and response.status_code == 200 else None
    job_list = []
    for i in range(len(data['items'])):
        job_list.append(data['items'][i]['id'])
    return job_list

# sc_id to joblist


def sc_to_joblist_map():
    map = {}
    for sc_id in sc_id_to_name:
        map[sc_id] = jobs_from_sc(sc_id_to_name[sc_id])


# LIST OF SC
list_skills = []
for s in sc_id_to_name:
    list_skills.append(s)


# LIST OF JOBS
url = "https://api.infojobs.net/api/7/offer?category=informatica-telecomunicaciones&maxResults=10"
response = requests.request("GET", url, headers=headers, data=payload)

data_5 = response.json() if response and response.status_code == 200 else None
data_5['items'][0]
