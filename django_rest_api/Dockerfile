FROM python:3@sha256:d2a7d3ef4e20e55e9ac8ba194e983dc7d2c8d012fd633a9d050ca8557399f2c2
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver"]