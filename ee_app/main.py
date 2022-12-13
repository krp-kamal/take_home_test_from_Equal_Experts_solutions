#! /usr/bin/python3

from flask import Flask, request
import socket

app = Flask(__name__)
## getting the hostname by socket.gethostname() method

hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method

ip_address = socket.gethostbyname(hostname)

@app.route('/', methods=['GET'])

def helloworld():
    if(request.method == 'GET'):
        data = "Hello World from -> " + ip_address
        return (data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
