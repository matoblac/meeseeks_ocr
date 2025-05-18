FROM python:3.10-slim

RUN apt update && apt install -y \
    tesseract-ocr \
    poppler-utils \
    libglib2.0-0 \
    libgl1 \
    && apt clean

WORKDIR /app
COPY . /app
RUN pip install -e .

ENTRYPOINT ["meeseeks-ocr"]
