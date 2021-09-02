from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
 
app =   FastAPI()

inventory = {
    'names': {'chinonso', 'ifeanyi', 'chimaroke', 'nnaemeka'},
    'age': {24,21, 19, 16},
    'one': {
        'name': 'milk',
        'price': 3.4,
        'brand': 'regular'
    }
}
info = {
    1: {
        'name': 'milk',
        'price': 3.4,
        'brand': 'regular'
    }
}
data = {}

class Item(BaseModel):
    name: str
    price:float
    brand: Optional[str] = None

@app.get("/")
def home():
    return {"data": "Fast-API"}

# @app.get('/details')
# def details():
#     return {"data": inventory}

@app.get('/details')
def details():
    return {"data": data}

# @app.get('/get-item/{item_id}')
# def get_item(item_id:int):
#     return info[item_id]

# @app.get('/get-item/{item_id}/{name}')
# def get_item(item_id:str, name:int): 
#     return inventory[item_id]

# Path allows us to add more constraint or tell a user the description of such route
# @app.get('/get-item/{item_id}')
# def get_item(item_id:str = Path(None, description= 'the slug of the item you viewed')):
#     return inventory[item_id]

# @app.get("/get-by-name")
# @app.get("/get-by-name{item_id}")
# def get_item(*,name: Optional[str]=None,test:int ):
# # def get_item(name: Optional[str]=None, ):
#     for item_id in info:
#         if info[item_id]['name'] == name:
#             return info[item_id]

    # return {'data': 'not found'}

@app.get("/get-by-name/{item_id}")
def get_item(*,name: Optional[str]=None ):
    for item_id in data:
        if data[item_id].name == name:
            return data[item_id]

    return {'data': 'not found'}

@app.post('/create/{item_id}')
def create_item(item_id:int,item:Item):
    if item_id in data:
        return {'error': 'item already exists'}
    data[item_id] = item
    return data[item_id]