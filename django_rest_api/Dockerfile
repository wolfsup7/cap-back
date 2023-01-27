FROM wolfsup7/k9:0.0.1
WORKDIR /manage
COPY manage.py .
ENTRYPOINT ["python", "manage.py"]
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver"]