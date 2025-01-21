from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
TOMTOM_API_KEY = '3YzQxwAFHF8yAMWxHfKrjbNN1U3WHarx'

@app.route('/route', methods=['POST'])
def get_route():
    data = request.json
    origin = data.get('origin')
    destination = data.get('destination')
    url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json"
    params = {
        'key': TOMTOM_API_KEY,
        'travelMode': data.get('travelMode', 'car'),
    }
    response = requests.get(url, params=params)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
