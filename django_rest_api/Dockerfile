FROM python:3@sha256:a5b723f5b78cb73300b647ff49fba4ceea22c5ec68c547fa3291978e6b692259
ENV PYTHONUNBUFFERED=1

WORKDIR /python3.11

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver"]