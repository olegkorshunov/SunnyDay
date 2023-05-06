from pathlib import Path

from PIL import Image

from src.tasks.celery import celery_app


@celery_app.task
def resize_image(img_path: str, new_width: int, new_height: int):
    path: Path = Path(img_path)
    img = Image.open(path)
    height, width = img.size
    rotate = False

    if height < width:
        rotate = True
        img = img.rotate(angle=90, expand=True)
        height, width = img.size

    ratio = height / width
    tmp_width = int(ratio * new_height)

    img = img.resize((tmp_width, new_height))
    img = img.crop(((tmp_width - new_width) // 2, 0, (tmp_width + new_width) // 2, new_height))

    if rotate:
        img = img.rotate(angle=-90, expand=True)

    img.save(f"src/frontend/static/images/{new_width}x{new_height}_{path.name}")
