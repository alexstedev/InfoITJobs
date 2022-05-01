import json
import requests
import pandas as pd

payload = {}
headers = {
    'Authorization': 'Basic MWVlZDc3ZDJjZTJjNDQwMThiYWRjM2U0MGJkOTY1Y2E6RFBqYzdkMVNjNUlsRzRGTXZNVlFwaFA    4S2tXdkU2d0lnU3FYOW5rZ1Z0S2JaTkVzK1o=',
    'Cookie': 'IJUSERUID=3b364be8-a072-47b8-bac4-34f29903ceb4; JSESSIONID=TJpfc6KysyOynUJQl3roTCKE'
}


def retrieve_data():
    # DICT sc-id to sc-str
    url = "https://api.infojobs.net/api/1/candidate/skillcategory?includeSkills=true"
    response = requests.request("GET", url, headers=headers)
    data_6 = response.json() if response and response.status_code == 200 else None
    sc_id_to_name = {}
    for i in range(len(data_6)):
        for j in range(len(data_6[i]['subcategories'])):
            if 1400 <= data_6[i]['subcategories'][j]['id'] <= 1499:
                sc_id_to_name[str(data_6[i]['subcategories'][j]['id'])
                              ] = data_6[i]['subcategories'][j]['name']
    # print(sc_id_to_name)
    with open('sc_id_to_name.json', 'w') as file:
        json.dump(sc_id_to_name, file)

    skills_id_to_name = {}

    for i in range(len(data_6)):
        for j in range(len(data_6[i]['subcategories'])):
            for k in range(len(data_6[i]['subcategories'][j]['skills'])):
                if 1400 <= data_6[i]['subcategories'][j]['id'] <= 1499:
                    skills_id_to_name[data_6[i]['subcategories'][j]['skills'][k]
                                      ['id']] = data_6[i]['subcategories'][j]['skills'][k]['name']
    with open('skills_id_to_name.json', 'w') as file:
        json.dump(skills_id_to_name, file, ensure_ascii=True)

    # Category matrix
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
                skills_vec.append(data_6[i]['subcategories'][j]['id'])
                category_matrix.append(skills_vec)

    with open('category_matrix.json', 'w') as file:
        json.dump(category_matrix, file, ensure_ascii=True)

    return sc_id_to_name, category_matrix, len(skills_id_to_name)


# problem with sc_list
