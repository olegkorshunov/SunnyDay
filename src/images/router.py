import shutil

from fastapi import APIRouter, UploadFile

from src.tasks.tasks import resize_image

router = APIRouter(
    prefix="/images",
    tags=["Add image"],
)


@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    path = f"src/frontend/static/images/{name}.webp"
    with open(path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
        resize_image.delay(path, 1024, 768)
        resize_image.delay(path, 224, 224)
