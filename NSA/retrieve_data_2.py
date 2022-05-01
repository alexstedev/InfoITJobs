import requests
import pandas as pd

payload = {}
headers = {
    'Authorization': 'Basic MWVlZDc3ZDJjZTJjNDQwMThiYWRjM2U0MGJkOTY1Y2E6RFBqYzdkMVNjNUlsRzRGTXZNVlFwaFA    4S2tXdkU2d0lnU3FYOW5rZ1Z0S2JaTkVzK1o=',
    'Cookie': 'IJUSERUID=3b364be8-a072-47b8-bac4-34f29903ceb4; JSESSIONID=TJpfc6KysyOynUJQl3roTCKE'
}


def jobs_from_sc(sc_name: str):  # given sc id
    url = "https://api.infojobs.net/api/7/offer?subcategory="+sc_name+"&maxResults=100"
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json() if response and response.status_code == 200 else None
    job_list = []
    if data is not None:
        for i in range(len(data['items'])):
            job_list.append(data['items'][i]['id'])
    return job_list


def retrieve_data():
    # DICT sc-id to sc-str
    url = "https://api.infojobs.net/api/7/offer?category=informatica-telecomunicaciones&maxResults=500"
    response = requests.request("GET", url, headers=headers, data=payload)
    data_2 = response.json() if response and response.status_code == 200 else None
    sc_id_to_name = {}
    for i in range(len(data_2['items'])):
        sc_id_to_name[data_2['items'][i]['subcategory']['id']
                      ] = data_2['items'][i]['subcategory']['value']

    url = "https://api.infojobs.net/api/1/candidate/skillcategory?includeSkills=true"
    response = requests.request("GET", url, headers=headers, data=payload)
    data_6 = response.json() if response and response.status_code == 200 else None
    for i in range(len(data_6)):
        for j in range(len(data_6[i]['subcategories'])):
            if 1400 <= data_6[i]['subcategories'][j]['id'] <= 1499:
                sc_id_to_name[data_6[i]['subcategories'][j]['id']
                              ] = data_6[i]['subcategories'][j]['name']
    sc_id_to_joblist = {}
    for sc_id in sc_id_to_name:
        sc_id_to_joblist[sc_id] = jobs_from_sc(sc_id_to_name[sc_id])

    skills_id_to_name = {}
    for i in range(len(data_6)):
        for j in range(len(data_6[i]['subcategories'])):
            for k in range(len(data_6[i]['subcategories'][j]['skills'])):
                if 1400 <= data_6[i]['subcategories'][j]['id'] <= 1499:
                    skills_id_to_name[data_6[i]['subcategories'][j]['skills'][k]
                                      ['id']] = data_6[i]['subcategories'][j]['skills'][k]['name']

    # Category matrix
        job_matrix = []

    for i in range(len(data_2['items'])):
        for sc in sc_id_to_name:
            job_vector = []
            if data_2['items'][i]['subcategory']['id'] == sc:
                job_vector.append(1)
            else:
                job_vector.append(0)
            job_vector += [data_2['items'][i]['subcategory']['id']]
        job_matrix.append(job_vector)

    return sc_id_to_joblist, job_matrix, len(skills_id_to_name)
# problem with sc_list
