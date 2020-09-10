from fastapi import FastAPI, Depends, WebSocket
from fastapi import BackgroundTasks, Request
from fastapi import Form

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
from fastapi.responses import RedirectResponse


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
    return templates.TemplateResponse("base.html", {"request" : request})

@app.get('/signup/', response_class=HTMLResponse)
def signup(request: Request, settings: config.Settings = Depends (get_settings)):
    return templates.TemplateResponse("signup.html", {"request" : request})

@app.get('/signup_welcome/{user_name}', response_class=HTMLResponse)
def signup_welcome(user_name: str, request: Request, settings: config.Settings = Depends (get_settings)):
    return templates.TemplateResponse("base.html", {"request" : request})


@app.post('/signup_action', response_class=RedirectResponse)
async def signup_action(user_name: str = Form (...)
                    , user_pass: str = Form (...)
                    , user_email: str = Form (...)
                    , settings: config.Settings = Depends (get_settings)):

    crud.add_user(settings.db_file
                  , user_name_value = user_name
                  , user_pass_value = user_pass
                  , primary_email_value = user_email)

    return RedirectResponse (url='/signup_welcome/{}'.format(user_name), status_code=302)
