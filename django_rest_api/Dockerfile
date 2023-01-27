FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /python3.11

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver"]