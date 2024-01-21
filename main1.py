from flask import Flask, request
import requests

app = Flask(__name__)

@api_endpoint = "http://rummynabob.4599vip.com/api/game/app/exclude/bindPhoneCodeNoImgCode"

@app.route('/send-sms', methods=['POST'])
def send_sms():
    try:
        data = request.get_json()
        phone_number = data['9336734442']
        
        payload = {
            "id": 0,
            "projectSign": "rummynabob",
            "phone": phone_number
        }

        response = requests.post(api_endpoint, json=payload)

        if response.status_code == 200:
            return f'SMS request sent successfully! Response: {response.json()}', 200
        else:
            return f'Failed to send SMS request. Status Code: {response.status_code}', 500

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

