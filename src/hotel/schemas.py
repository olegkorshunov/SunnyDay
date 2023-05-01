from pydantic import BaseModel


class Shotel(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int

    class Config:
        orm_mode = True


class SHotelsWithRoomsLeft(Shotel):
    rooms_left: int  # number of available rooms

    class Config:
        orm_mode = True
