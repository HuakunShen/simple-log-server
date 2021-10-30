from flask import Flask, request
import logging
from send_email import send_email

logging.basicConfig(filename='log.log', level=logging.CRITICAL, format="%(asctime)s | %(levelname)s | %(message)s")
app = Flask(__name__)


@app.route('/', methods=['POST'])
def log():
    if 'data' in request.form:
        app.logger.critical(request.form['data'])
        return "logged"
    return "no data in request"


@app.route('/email', methods=['POST'])
def email():
    if 'data' in request.form:
        send_email("From Simple Log Server", request.form['data'])
        return "emailed"
    return "no data in request"


if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0")
