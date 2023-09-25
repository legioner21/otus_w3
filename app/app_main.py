from fastapi import FastAPI

from api import api_router
from app_config import settings

app = FastAPI(title=settings.PROJECT_NAME, docs_url="/")
app.include_router(api_router, prefix=settings.API_V1_STR)
