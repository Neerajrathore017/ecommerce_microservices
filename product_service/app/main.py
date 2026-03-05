from fastapi import FastAPI
from app.api.product_routes import router

app = FastAPI(title="Product Service")

app.include_router(router)
