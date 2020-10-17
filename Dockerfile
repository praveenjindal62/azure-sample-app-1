FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8080
CMD ["flask","run"]
