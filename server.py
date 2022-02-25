import os
from flask import Flask, request, Response
import logging
from send_email import send_email

logging.basicConfig(filename='log.log', level=logging.CRITICAL, format="%(asctime)s | %(levelname)s | %(message)s")
app = Flask(__name__)

RECEIVER_ADDRESS = os.environ.get('RECEIVER_ADDRESS')
X_API_KEY = os.environ.get("X_API_KEY")


@app.route('/', methods=['POST'])
def log():
    if 'data' in request.form:
        app.logger.critical(request.form['data'])
        return "logged"
    return "no data in request"


@app.route('/email', methods=['POST'])
def email():
    if X_API_KEY is not None:
        if 'X-Api-Key' not in request.headers or request.headers['X-Api-Key'] != X_API_KEY:
            return Response("Not Authorized", status=401, mimetype='application/text')
    if 'data' in request.form:
        print(request.form['data'])
        if send_email("Subject: Simple Log Server", request.form['data'], RECEIVER_ADDRESS):
            print(request.form['data'])
            return "emailed"
        else:
            app.logger.error('ERROR: cannot send email')
            return "no email"
    return Response("no data in request", status=400, mimetype='application/text')


if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0")
