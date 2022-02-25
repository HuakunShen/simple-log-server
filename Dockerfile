FROM python:3.11.0a1-alpine3.14
RUN pip install Flask==2.0.3 && pip install python-dotenv==0.19.2
WORKDIR /root/simple-log-server
COPY . .
CMD python server.py