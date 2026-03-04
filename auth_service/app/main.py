from fastapi import FastAPI
from app.routes.auth_routes import router

app = FastAPI(title="Auth Service")

app.include_router(router)