FROM python:3@sha256:e7e3b031dbf71514d0a8d759d8417b04f8dcf483aec18d69abd1a2b3955297b6
ENV PYTHONUNBUFFERED=1

WORKDIR /python3.11

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver"]