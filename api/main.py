from typing import Optional
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Skills(BaseModel):
    skills: dict

skill: Optional[Skills] = None

app = FastAPI()

origins = [
        "http://localhost",
        "http://localhost:4200",
        ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )


headers = {
        'Authorization': 'Basic MWVlZDc3ZDJjZTJjNDQwMThiYWRjM2U0MGJkOTY1Y2E6RFBqYzdkMVNjNUlsRzRGTXZNVlFwaFA    4S2tXdkU2d0lnU3FYOW5rZ1Z0S2JaTkVzK1o=',
        'Cookie': 'IJUSERUID=3b364be8-a072-47b8-bac4-34f29903ceb4; JSESSIONID=TJpfc6KysyOynUJQl3roTCKE'
        }

@app.get("/categories")
async def categories():
    url = "https://api.infojobs.net/api/1/candidate/skillcategory"
    response = requests.request("GET", url, headers=headers)
    data = response.json() if response and response.status_code == 200 else None

    for i in range(len(data)):
        if data[i]['id'] == 14:
            return data[i]['subcategories']

    return None

@app.get("/condensed_categories")
async def condensed_categories():
    url = "https://api.infojobs.net/api/1/candidate/skillcategory"
    response = requests.request("GET", url, headers=headers)
    data = response.json() if response and response.status_code == 200 else None

    for i in range(len(data)):
        if data[i]['id'] == 14:
            it_skills = {}
            for j in range(len(data[i]['subcategories'])):
                it_skills[data[i]['subcategories'][j]['id']] = data[i]['subcategories'][j]['name']
            return it_skills

    return None

@app.get("/condensed_skills")
async def condensed_skills(): # category: str | None = None
    url = 'https://api.infojobs.net/api/1/candidate/skillcategory?includeSkills=true'
    response = requests.request("GET", url, headers=headers)
    data = response.json() if response and response.status_code == 200 else None
    skills_id_to_name = {}
    for i in range(len(data)):
        for j in range(len(data[i]['subcategories'])):
            for k in range(len(data[i]['subcategories'][j]['skills'])):
                if 1401 <= data[i]['subcategories'][j]['id'] <= 1499:
                    skills_id_to_name[data[i]['subcategories'][j]['skills'][k]['id']] = data[i]['subcategories'][j]['skills'][k]['name']

    return skills_id_to_name

@app.post("/update_user_skills")
async def update_user_skills(_user_skills: Skills):
    skill = _user_skills 
    return item

@app.get("/user_skills")
async def user_skills():
    return skills

@app.get("/offers")
async def offers(category: Optional[str] = None, page: Optional[int] = None):
    url = 'https://api.infojobs.net/api/7/offer?category=informatica-telecomunicaciones'
    if category:
        url += '&subcategory=' + category
    if page:
        url += '&page=' + str(page)
    response = requests.request("GET", url, headers=headers)
    data = response.json() if response and response.status_code == 200 else None
    return data
    
@app.get("/all_offers")
async def all_offers():

    url = 'https://api.infojobs.net/api/7/offer?category=informatica-telecomunicaciones&page='
    response = requests.request("GET", url + '1', headers=headers)
    data = response.json() if response and response.status_code == 200 else None
    
    max_pages = data['totalPages']
    for i in range(2, 5):
        response = requests.request("GET", url + str(i), headers=headers)
        temp_data = response.json() if response and response.status_code == 200 else None
        data['items'] += temp_data['items']

    return data

    


@app.get("/cities")
async def cities():
    url = 'https://api.infojobs.net/api/1/dictionary/city'
    response = requests.request("GET", url, headers=headers)
    data = response.json() if response and response.status_code == 200 else None
    return data



#@app.get("/skills")
#async def skills(subcategoryId: int | None = None):



