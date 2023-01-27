FROM python:3@sha256:6b85854518f812d94cf2dfee2386df85b9cb78835a872d4769b4335f584c43ba

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver"]