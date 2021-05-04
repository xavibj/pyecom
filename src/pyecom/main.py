from fastapi import FastAPI
from starlette.requests import Request
from pydantic import BaseModel
from typing import List, Optional

import yaml
import mysql.connector


app = FastAPI()

with open('/etc/pyecom.yml', 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Product(BaseModel):
    codigo: str
    reference: str

@app.get("/products", response_model=List[Product])
async def products(request: Request, skip: int = 0, limit: int = 10):
    print(request.query_params)
    if "codigo" in request.query_params:
        codigo = request.query_params['codigo']
    else:
        codigo = None
    cp = config['products']
    cnx = mysql.connector.connect(
        user = cp['database']['user'], 
        password = cp['database']['pwd'],
        host = cp['database']['host'],
        database = cp['database']['db'])

    cursor = cnx.cursor(dictionary=True)
    query = ("SELECT codigo, reference FROM ps_product WHERE active=1 {} LIMIT {},{}".format("and codigo like '%"+codigo+"%'" if codigo else '', skip, limit))
    print(query)
    cursor.execute(query)

    product_list = cursor.fetchall()

    cursor.close()
    cnx.close()

    return product_list