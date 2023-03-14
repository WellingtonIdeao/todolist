# syntax=docker/dockerfile:1
# Builder stage
FROM python:3.11.2-slim-buster AS builder

RUN apt update && \
    apt install -y libpq-dev gcc

# Create the virtual environment
RUN python -m venv /opt/venv
# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install  -r requirements.txt

# Operational stage
FROM python:3.11.2-slim-buster

RUN apt update && \
    apt install -y libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Get the virtual enviroment form builder stage
COPY --from=builder /opt/venv/ /opt/venv

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR	/app

COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

