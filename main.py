from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


# class FoodEnum(str, Enum):
#     fruit = "apple"
#     vegitable = "carrot"
#     dairy = "dairy"


# @app.get("/")
# async def root():
#     return {"msg": "Hello World"}


# @app.post("/")
# async def post():
#     return {"msg": "hello from Post route"}


# @app.get("/users")
# async def list_item():
#     return {"msg": "All item"}


# # params pass
# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     return {"msg": user_id}


# @app.get("/food/{food_name}")
# async def get_food(food_name: FoodEnum):
#     print(food_name)
#     return {"msg": food_name}


# # query params
# fake_item = [{"item_name": "apple"}, {"item_name": "orange"},
#              {"item_name": "mango"}, {"item_name": "pineapple"}]


# @app.get("/items")
# async def list_items(skip: int | None = 0, limit: int | None = 0):
#     return fake_item[skip: skip+limit]


# # Request Body

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.post("/items")
# async def create_item(item: Item):
#     pass


# @app.put("/items/{item_id}")
# async def update_item_by_id(item_id: int, item: Item, q: str | None = None):
#     item_dict = {"id": item_id, **item.dict()}
#     if q:
#         item_dict.update({"q": q})
#     return item_dict


# validation Part

# @app.post("/item")
# async def validate_query(q: str | None = Query(None, min_length=3, max_length=10)):
#     return q

# @app.post("/item")
# async def validate_query(q: list[str] = Query(['Sachin', "sam"])):
#     return q

# class Item(BaseModel):
#     name: str
#     age: int


# class ItemDesc(BaseModel):
#     id: int
#     desc: str


# @app.post("/item/{item_id}")
# async def create_item(
#         *,
#         item_id: int = Path(..., title="Provide the Id"),
#         q: str | None = None,
#         item: Item = Body(..., embed=True),
#         # item_desc: ItemDesc,
#         # cost: int = Body(...)
# ):
#     result = {"id": item_id}
#     if q:
#         result.update({"q": q})
#     if item:
#         result.update({"item": item})
#     # if item_desc:
#     #     result.update({"item_desc": item_desc})
#     # if cost:
#     #     result.update({"cost": cost})
#     return result
