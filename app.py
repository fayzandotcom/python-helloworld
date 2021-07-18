from flask import Flask,json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
  app.logger.info('Main request successfull')
  return "Hello World!"

@app.route("/status")
def status():
  app.logger.info('Status request successfull')
  response = app.response_class(
    response = json.dumps({ "result": "OK - healthy"}),
    status = 200,
    mimetype = 'application/json'
  )
  return response

@app.route("/metrics")
def metrics():
  app.logger.info('Metrics request successfull')
  response = app.response_class(
    response = json.dumps({ "data" : { "UserCount": 140, "UserCountActive": 23}}),
    status = 200,
    mimetype = 'application/json'
  )
  return response

if __name__ == "__main__":
  # logging.basicConfig(filename='app.log', level=logging.DEBUG)
  app.run(debug=True)
