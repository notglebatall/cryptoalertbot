import time
import warnings
import logging
warnings.filterwarnings("ignore", category=UserWarning, module='telegram.utils.request')

from flask import Flask, request, jsonify
from handler import send_alert, send_test_message

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp


@app.route("/webhook", methods=["POST"])
def webhook():
    whitelisted_ips = ['52.89.214.238', '34.212.75.30', '54.218.53.128', '52.32.178.7']
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if client_ip not in whitelisted_ips:
        print(client_ip)
        return jsonify({'message': 'Unauthorized'}), 401
    try:
        if request.method == "POST":
            data = request.get_json()
            print(get_timestamp(), "Alert Received & Sent!")
            send_alert(data)
            return jsonify({'message': 'Webhook received successfully'}), 200

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        return jsonify({'message': 'Error'}), 400


if __name__ == "__main__":
    send_test_message('Bot started')

    from waitress import serve
    serve(app, host="0.0.0.0", port=80)


