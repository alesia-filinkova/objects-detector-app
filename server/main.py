from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world!"}

items = {
    1: {"name": "Item one", "description": "This is the first item"},
    2: {"name": "Item two", "description": "This is the second item"},
    3: {"name": "Item three", "description": "This is the third item"},
}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    
    if item is None:
        return {"error": "Item not found"}, 404
    
    return item
