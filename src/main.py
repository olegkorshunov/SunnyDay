import uvicorn
from fastapi import FastAPI

import src.models  # noqa
from src.auth.router import router as auth_router
from src.booking.router import router as booking_router
from src.hotel.room.router import router as room_router  # noqa
from src.hotel.router import router as hotel_router

app = FastAPI()


app.include_router(booking_router)
app.include_router(auth_router)
app.include_router(hotel_router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
