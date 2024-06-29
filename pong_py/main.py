import os
from flask import Flask, jsonify

app = Flask(__name__)

def get_addr():
    addr = ":8080"
    from_env = os.getenv("PONG_LISTENING_ADDRESS")

    if from_env:
        addr = from_env

    if len(os.sys.argv) > 1:
        addr = os.sys.argv[1]

    return addr

@app.route('/ping/<param>', methods=['GET'])
def ping(param):
    return jsonify({"pong": param})

if __name__ == '__main__':
    addr = get_addr()
    host, port = addr.split(':')
    app.run(host=host, port=int(port))
