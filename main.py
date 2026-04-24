from fastapi import FastAPI, Request, staticfiles
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
import sqlite3
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse

app = FastAPI()

origins = [
    'http://localhost:8000',
    'http://0.0.0.0:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

os.makedirs('static', exist_ok=True)

app.mount('/static', staticfiles.StaticFiles(directory='static'), name='static')

class Weather(BaseModel):
    temperature: float
    humidity: float

@app.get('/api/weather')
async def read_weather():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('SELECT temperature, humidity FROM weather')
    rows = c.fetchall()
    conn.close()
    return [{'temperature': row[0], 'humidity': row[1]} for row in rows]

@app.get('/')
async def read_root(request: Request):
    return HTMLResponse('static/index.html')