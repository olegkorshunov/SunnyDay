# SunnyDay
How to up service: 
1. Create an `.env` file using the `.example.env`
2. Use docker
```
docker compose build
docker compose up
```

[http://localhost:8000/docs](http://localhost:8000/docs) - docs  
[http://localhost:8000/pages](http://localhost:8000/pages) - frontend  
[http://localhost:8000/admin](http://localhost:8000/admin) - admin panel  
[http://localhost:5555/](http://localhost:5555/) - flower  


This is my pet project, about booking hotels.  Here I will used the following technologies:
 * FastAPI, JWT
 * SQLAlchemy 2.0, PostgreSQL, Alembic, SQL, SQLAdmin
 * Redis, Celery, Flower
 * Docker
