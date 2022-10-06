from python:3.9-alpine

WORKDIR .
COPY . .

RUN python3.9 -m pip install -r requirements.txt

EXPOSE 9300

CMD ["gunicorn", "-b", "0.0.0.0:9300", "-w", "2", "app:app"]
