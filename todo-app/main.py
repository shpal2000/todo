from fastapi import FastAPI, Depends, WebSocket, BackgroundTasks, Request

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
def root(request: Request, settings: config.Settings = Depends (get_settings)):
    return templates.TemplateResponse("base.html", {"request" : request, "id" : 10})

@app.get('/signup', response_class=HTMLResponse)
def root(request: Request, settings: config.Settings = Depends (get_settings)):
    return templates.TemplateResponse("signup.html", {"request" : request, "id" : 10})


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
