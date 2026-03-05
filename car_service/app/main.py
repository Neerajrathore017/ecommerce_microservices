from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.cart_routes import router

app = FastAPI(title="Cart Service")

Base.metadata.create_all(bind=engine)

app.include_router(router)
# from fastapi import FastAPI
# from app.api.cart_routes import router

# app = FastAPI(title="Cart Service")

# app.include_router(router)
