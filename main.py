from contextlib import asynccontextmanager


from fastapi import FastAPI, Request
from db.database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware

from db.create_database import create_tables
from routers import (test, user, travel)


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

# Aqui incluimos a função do router do ficheiro que pretendemos usar
app.include_router(prefix="/api", router=test.router)
# Exemplo: app.include_router(prefix="/api", router=travel.router)
app.include_router(prefix="/api", router=user.router)
app.include_router(prefix="/api", router=travel.router)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response

# Endpoint de health se for preciso dar ping para verificar se funciona
@app.get("/api/health")
async def main():
    return {"Hello": "from my api!"}