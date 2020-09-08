from fastapi import FastAPI, Depends, WebSocket, BackgroundTasks

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from typing import Optional, List
from pydantic import BaseModel

from functools import lru_cache

import time

import sqlite3
import crud
import config

from fastapi.responses import ORJSONResponse
from fastapi.responses import HTMLResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@lru_cache
def get_settings():
    settings = config.Settings()
    crud.create_tables (settings.db_file)
    return settings

@app.on_event("startup")
def startup():
    print ("startup")


@app.on_event("shutdown")
def shutdown():
    print ("shutdown")


@app.get('/', response_class=HTMLResponse)
def root(settings: config.Settings = Depends (get_settings)):
    response = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="todo">
    <meta name="author" content="shpal2000">

    <title>todo</title>

  </head>

  <body>
    <h1>hello todo</h1>
    <script src="{{ url_for('static', path='/js/jquery-3.3.1.slim.min.js') }}"></script>
  </body>
</html>
     '''
    return HTMLResponse(content=response, status_code=200)

class NewUser(BaseModel):
    user_name: str
    user_pass: str
    full_name: str
    primary_email: str
    primary_phone: str

@app.post('/add_user', response_class=ORJSONResponse)
async def add_user(params : NewUser
                    , settings: config.Settings = Depends (get_settings)):

    crud.add_user(settings.db_file, 
                  params.user_name,
                  params.user_pass,
                  params.full_name,
                  params.primary_email,
                  params.primary_phone)

    return params
