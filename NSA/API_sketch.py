from fastapi import FastAPI
app = FastAPI()


@app.get("/my-first-api")
def hello():
    import json

    path = "cualsevol.json"
    with open(path) as file:
        data = json.load(file)

    return data[0]
