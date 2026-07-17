from fastapi import FastAPI
from api import category_api, product_api
import uvicorn

marketplace_app = FastAPI(title='MarketPLace FastAPI Product')
marketplace_app.include_router(category_api.category_router)
marketplace_app.include_router(product_api.product_router)


if __name__ == '__main__':
    uvicorn.run(marketplace_app, host='127.0.0.1', port=8001)
