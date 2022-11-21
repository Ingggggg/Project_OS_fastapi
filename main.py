from fastapi import FastAPI
from routers import restaurant

app = FastAPI()

app.include_router(restaurant.router)