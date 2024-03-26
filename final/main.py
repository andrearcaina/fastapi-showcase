from fastapi import FastAPI, HTTPException

app = FastAPI()

# in memory database with ID of people with name, age, and major
db = {
    "1": {"name": "Mo", "age": 20, "major": "CS"},
    "2": {"name": "Jack", "age": 21, "major": "CE"},
    "3": {"name": "Andre", "age": 22, "major": "SE"},
    "4": {"name": "Joseph", "age": 23, "major": "EE"},
}

# base
@app.get("/")
async def root():
    return {"message": "Type /docs to see the swagger UI!"}

# return entire database
@app.get("/get/db")
async def get_db():
    return db

# get certain item by ID
@app.get("/get/{id}")
async def get_value_by_id(id: str):
    if id not in db:
        raise HTTPException(404, "Item not found in database!")
    return db[id]

# post to create a new item by ID
@app.post("/post/{id}")
async def create_value(id: str, name: str, age: int, major: str):
    if id in db:
        raise HTTPException(404, "Item already exists in database!")
    db[id] = {"name": name, "age": age, "major": major}
    return f"Successfully added item {id}"

# put to update an item by ID
@app.put("/put/{id}")
async def update_value(id: str, name: str, age: int, major: str):
    if id not in db:
        return HTTPException(404, "No such item in database!")
    db[id] = {"name": name, "age": age, "major": major}
    return f"Successfully updated item {id}"

# delete to delete an item by ID
@app.delete("/delete/{id}")
async def delete_value(id: str):
    if id not in db:
        return HTTPException(404, "No such item in database!")
    db.pop(id)
    return f"Successfully deleted item {id}"
