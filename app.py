from flask import Flask, request, Response
import requests, json      

app = Flask(__name__)

@app.route('/webhook', methods=["POST"])

def webhook():
	print("Request received!")
	print(request.json);
	return relay(request.json)

	
def relay(data):	
	print("Relaying Request with data :" + json.dumps(data))
	response = requests.post('REPLACEWITHDISCORDWEBHOOKURL_KEEPITSECRET', json=data) 
	print(response.status_code) 
	print(response.text) 
	return Response(status=response.status_code)
