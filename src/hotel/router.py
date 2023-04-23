from datetime import date

from fastapi import APIRouter

router = APIRouter(
    prefix="hotels",
    tags=["Hotel"],
)


@router.get("/{hotel_id}/rooms")
def get_all_rooms(hotel_id: int, date_from: date, date_to: date):
    pass
