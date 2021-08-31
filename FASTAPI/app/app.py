from fastapi import FastAPI
from datetime import date

app = FastAPI()

@app.get("/", tags=['ROOT'])  # get all data
async def root() -> dict:
    return{"data":cars}

@app.get('/car/{id}', tags=['cars'])
async def get_car(id:int) -> dict:
    for car in cars:
        if int(car["id"]) == id:
            return car
    return { "data": f"car with id {id} is not found !" }


@app.post('/car', tags=['cars'])
async def add_car(car:dict) -> dict:
    cars.append(car)
    return {
        "data": "A car has been added !"
    }
    
@app.put("/car/{id}", tags=['cars'])
async def update_car(id:int, body:dict) -> dict:
    for car in cars:
        if int(car["id"]) == id:
            car["Activity"] = body["Activity"]
            return { "data": f"car with id {id} has been updated !"}
    return { "data": f"car with id {id} is not found !" }


@app.delete("/car/{id}", tags=['cars'])
async def delete_car(id:int) -> dict:
    for car in cars:
        if int(car["id"]) == id:
            cars.remove(car)
            return { "data": f"car with id {id} has been deleted !"}
    return { "data": f"car with id {id} is not found !" }

cars = [
    {
	"id": "1",
	"name": "car_1",
	"mileage": 32.24, 
	"created_at": date(2021, 6, 24)
    },

    {
	"id": "2",
	"name": "car_2",
	"mileage": 252.14, 
	"created_at": date(2021, 8, 24)
    },
]