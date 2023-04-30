from pydantic import BaseModel


class SHotelsWithRoomsLeft(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int
    rooms_left: int  # number of available rooms

    class Config:
        orm_mode = True
