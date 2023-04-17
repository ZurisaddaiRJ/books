FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /books
WORKDIR /books
COPY requirements.txt /books/
RUN pip install -r requirements.txt
COPY . /books/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080
