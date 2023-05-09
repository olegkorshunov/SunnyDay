from celery import Celery

from src.config import settings

celery_app = Celery(
    main="tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include="src.tasks.tasks",
)
