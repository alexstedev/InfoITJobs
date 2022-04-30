import requests
import pandas as pd

payload = {}
headers = {
    'Authorization': 'Basic MWVlZDc3ZDJjZTJjNDQwMThiYWRjM2U0MGJkOTY1Y2E6RFBqYzdkMVNjNUlsRzRGTXZNVlFwaFA    4S2tXdkU2d0lnU3FYOW5rZ1Z0S2JaTkVzK1o=',
    'Cookie': 'IJUSERUID=3b364be8-a072-47b8-bac4-34f29903ceb4; JSESSIONID=TJpfc6KysyOynUJQl3roTCKE'
}


url = "https://api.infojobs.net/api/1/candidate/skillcategory"
response = requests.request("GET", url, headers=headers, data=payload)
data_1 = response.json() if response and response.status_code == 200 else None
# DICT sc_id to sc_name
sc_id_to_name = {}
for i in range(len(data_1)):
    if data_1[i]['id'] == 14:
        for j in range(len(data_1[i]['subcategories'])):
            sc_id_to_name[data_1[i]['subcategories'][j]['id']
                          ] = data_1[i]['subcategories'][j]['name']


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


url = "https://api.infojobs.net/api/1/candidate/skillcategory?includeSkills=true"
response = requests.request("GET", url, headers=headers, data=payload)
data_6 = response.json() if response and response.status_code == 200 else None
skills_id_to_name = {}
for i in range(len(data_6)):
    for j in range(len(data_6[i]['subcategories'])):
        for k in range(len(data_6[i]['subcategories'][j]['skills'])):
            if 1401 <= data_6[i]['subcategories'][j]['id'] <= 1499:
                skills_id_to_name[data_6[i]['subcategories'][j]['skills'][k]
                                  ['id']] = data_6[i]['subcategories'][j]['skills'][k]['name']

category_matrix = []
for i in range(len(data_6)):
    for j in range(len(data_6[i]['subcategories'])):
        skills_vec = []
        if 1401 <= data_6[i]['subcategories'][j]['id'] <= 1499:
            category_skills = []
            for k in range(len(data_6[i]['subcategories'][j]['skills'])):
                category_skills.append(
                    data_6[i]['subcategories'][j]['skills'][k]['id'])
            for sk in skills_id_to_name:
                if sk in category_skills:
                    skills_vec.append(1)
                else:
                    skills_vec.append(0)
            category_matrix.append(skills_vec)
print(category_matrix)
