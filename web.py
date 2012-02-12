import os
from flask import Flask, request, jsonify

app = Flask(__name__)
state = {}

@app.route('/')
def index():
  return open('html/index.html').read()

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.debug = True
  app.run(host='0.0.0.0', port=port)

