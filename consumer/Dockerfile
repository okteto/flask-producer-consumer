FROM python:3.8

COPY requirements.txt .
RUN apt-get install libxml2-dev libxslt-dev
RUN pip install -r requirements.txt
WORKDIR /code

COPY ./src .

CMD ["python", "app.py"]
