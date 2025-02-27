FROM python:3.11

WORKDIR /app

COPY ./requirments.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED=1

CMD ["python", "/app/server.py","--port=8000"]