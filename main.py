from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_database, delete_database
from router import router as task_ruter


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database()
    yield
    await delete_database()


app = FastAPI(
    title="CURD_KA_PAIN", lifespan=lifespan
)
app.include_router(task_ruter)
