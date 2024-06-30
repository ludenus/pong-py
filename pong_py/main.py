import os
from flask import Flask, Response, jsonify

app = Flask(__name__)

def get_addr():
    addr = os.getenv("PONG_LISTENING_ADDRESS", ":8080")
    return addr

def load_config():
    config_file = os.getenv("PONG_CONFIG_FILE", "config.yaml")
    try:
        with open(config_file, 'rb') as file:  # Read as bytes
            content = file.read()
    except FileNotFoundError:
        content = None
    return content, config_file

config_content, config_file = load_config()

@app.route('/ping/<param>', methods=['GET'])
def ping(param):
    return jsonify({"pong": param})

@app.route('/config', methods=['GET'])
def get_config():
    if config_content is None:
        return jsonify({"error": f"Config file '{config_file}' not found."}), 404
    return Response(config_content, mimetype='text/plain')

if __name__ == '__main__':
    addr = get_addr()
    host, port = addr.split(':')
    app.run(host=host, port=int(port))
