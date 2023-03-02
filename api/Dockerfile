FROM python:3.10-slim as base

WORKDIR /src/

COPY ./requirements.txt /src/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/app/requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/src/app

COPY . /src/app

FROM base AS build

# 
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]