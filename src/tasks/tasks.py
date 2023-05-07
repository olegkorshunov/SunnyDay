import smtplib
from pathlib import Path

from PIL import Image
from pydantic import EmailStr

from src.config import settings
from src.tasks.celery import celery_app
from src.tasks.email_templates import create_booking_confirmation_template


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


@celery_app.task
def send_booking_confirmation_email(
    booking: dict,
    email_to: EmailStr,
):
    email_to_mock = settings.SMTP_USER
    # Since in database all email address is fakes,
    # for checking if everything is work,
    # we send confirm to self
    msg_content = create_booking_confirmation_template(booking, email_to_mock)  # email_to
    with smtplib.SMTP_SSL(host=settings.SMTP_HOST, port=settings.SMTP_PORT) as server:
        server.login(user=settings.SMTP_USER, password=settings.SMTP_PASS)
        server.send_message(msg=msg_content)
