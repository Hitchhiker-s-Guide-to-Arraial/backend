from contextlib import asynccontextmanager


from fastapi import FastAPI, Request
from db.database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware

from db.create_database import create_tables
from routers import (test)


@asynccontextmanager
async def lifespan(app):
    create_tables()
    yield

app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs", redoc_url="/api/redoc",
                lifespan=lifespan,
                title="API",
                description="API description"
                )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prefix="/api", router=test.router)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/health")
async def main():
    return {"Hello": "from my api!"}