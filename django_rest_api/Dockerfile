FROM python:3

ENV PYTHONUNBUFFERED=1
ENV k9back=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver