from fastapi import FastAPI
import httpx

app = FastAPI(title="API Gateway")

AUTH_URL = "http://127.0.0.1:8001"
PRODUCT_URL = "http://127.0.0.1:8002"


@app.get("/login")
async def login():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{AUTH_URL}/login")
        return res.json()


@app.get("/products")
async def products():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{PRODUCT_URL}/products")
        return res.json()