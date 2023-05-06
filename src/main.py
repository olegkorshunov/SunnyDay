from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

import src.models  # noqa
from src.auth.router import router as auth_router
from src.booking.router import router as booking_router
from src.config import settings
from src.frontend.pages.router import router as router_pages
from src.hotel.room.router import router as room_router  # noqa
from src.hotel.router import router as hotel_router
from src.images.router import router as image_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(settings.REDIS_URL, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield
    # SHUTDOWN


app = FastAPI(lifespan=lifespan)


app.mount(path="/static", app=StaticFiles(directory="src/frontend/static"), name="static")

app.include_router(booking_router)
app.include_router(auth_router)
app.include_router(hotel_router)

app.include_router(router_pages)
app.include_router(image_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
