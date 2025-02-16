FROM python:3.9
RUN pip install --upgrade pip

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

RUN pip install uvicorn

COPY ./src/ /home/app/src/

WORKDIR /home/app/

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8080"]