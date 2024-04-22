FROM python:3

WORKDIR /app
COPY . .
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

