import shutil

from fastapi import APIRouter, UploadFile

router = APIRouter(
    prefix="/images",
    tags=["Add image"],
)


@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    with open(f"src/frontend/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
