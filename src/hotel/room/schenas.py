from typing import Optional

from pydantic import BaseModel


class SUnbookedRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: Optional[str]
    services: list[str]
    price: int
    quantity: int
    image_id: int
    total_cost: int
