import os
from typing import Annotated
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from router import users
from router import events

app = FastAPI()

#access rules

origins = [
    "*",
    "http://localhost",
    "http://localhost:8000",
    "http://192.168.0.41:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(events.router)

@app.get("/")
async def root():
    return {'status':'ok'}

if __name__ == "__main__":
    uvicorn.run(app)
