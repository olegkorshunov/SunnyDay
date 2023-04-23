from fastapi import APIRouter

router = APIRouter(
    prefix="/hotels",
    tags=["Hotel"],
)


@router.get("")
def get_hotels_with_available_rooms():
    pass
