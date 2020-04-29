FROM python:3.8

LABEL author="Andy"
LABEL description="Dockerfile for Plan Scraping"

COPY main.py /code/

COPY requirements.txt /code/

WORKDIR /code/

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
