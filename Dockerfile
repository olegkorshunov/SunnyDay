FROM python:3.10

WORKDIR /sunnyday

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /sunnyday/docker_scripts/*.sh
