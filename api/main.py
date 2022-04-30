import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/offers")
async def offers(category: str | None = None):
    url = 'https://api.infojobs.net/api/7/offer'
    if category:
        url += '?subcategory=' + category
    else:
        url += '?category=informatica-telecomunicaciones'
    response = requests.request("GET", url, headers=headers)
    data = response.json() if response and response.status_code == 200 else None
    
    return data

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

    


#@app.get("/skills")
#async def skills(subcategoryId: int | None = None):



