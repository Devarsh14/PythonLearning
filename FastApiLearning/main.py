from fastapi import FastAPI, Query
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# create new end point which returns the list of coffee types
@app.get("/coffee")
def read_coffee():
    return {"Coffee": ["Espresso", "Americano", "Cappuccino"]}

# create new end point whcih returns the list of animal types
@app.get("/animals")
def read_animals():
    return {"dog", "cat", "rabbit"}

@app.get("/queryTest")
def query_test(q_type: str= Query(None)):
    if q_type is not None:
        return {"q_type": q_type}
    else:
        return {"q_type": "No query parameter passed"}


# create dictionary of car brands and models
cars = {
    "Toyota": ["Corolla", "Camry", "RAV4"],
    "Honda": ["Civic", "Accord", "CR-V"],
    "Ford": ["Focus", "Fusion", "Escape"]
}


@app.get("/cars")
def read_cars(car_brand: str = Query(None)):
    if car_brand is not None:
        return {car_brand: cars[car_brand]}
    else:
        return "No car brand passed"

# To run python main.py
# uvicorn main:app --reload
# pip list | grep fastapi
# pip freeze > requirements.txt
# source myenv/bin/activate