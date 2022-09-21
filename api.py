from asyncore import write
import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/callback/', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    print(content_type)

    if (content_type == 'application/json'):
        jsonBody = request.json

        print(jsonBody)

        session = requests.Session()

        SALESFORCE_OAUT_URL = 'https://teaminternational1234--dreamforce.sandbox.my.salesforce.com/services/oauth2/token'
        params = {
            "grant_type": "password",
            "client_id": "3MVG9AYugMwGAhY4ZG_h9jrqP3jdLt..udfMePvQYAyaCTZKGPvKHp8zA3kl50PlOhNtQXRUjRczVB3_.5sjp",
            "client_secret": "2990BCBBB657D05E3765CBE3C2F1FFE1E16AC838B659B195F231DBD2854027B6",
            "username": "luciano.straga@teaminternational.com.dreamforce",
            "password": "dni35373784.P76hS7pkojWLDpUgr42ELikcm"
        }

        authResponse = session.post(SALESFORCE_OAUT_URL, params=params)
        parsedAuthResponse = authResponse.json()

        accessToken = parsedAuthResponse.get("access_token")
        instanceUrl = parsedAuthResponse.get("instance_url")

        SALESFORCE_SERVICE = instanceUrl + '/services/data/v55.0/sobjects/Marketing_Cloud_Event__e/'
    
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+accessToken
        }

        requestToSend = {
            "Payload__c" : json.dumps(jsonBody),
        }
        payload = json.dumps(requestToSend)

        #response = requests.request("POST", SALESFORCE_SERVICE, headers=headers, data=payload)
    
        return '201'
    else:
        return 'Content-Type not supported!'

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Flask REST API</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)