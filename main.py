from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as file:
        data = json.load(file)
    return data

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error': 'patient not found'}