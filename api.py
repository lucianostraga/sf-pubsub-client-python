from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/callback/', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Flask REST API</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)