import uuid
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    request_id = uuid.uuid4()
    print(f'API 요청 ID={request_id}')
    return 'Hello World'
if __name__ == '__main__':
    app.run()

'''
API 요청 ID=3233e18a-2de3-4aae-9900-c68bead72b5e
127.0.0.1 - - [10/May/2021 11:47:58] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/May/2021 11:47:58] "GET /favicon.ico HTTP/1.1" 404 -
API 요청 ID=5e276c68-0aeb-447c-968e-255d5d6ebdac
127.0.0.1 - - [10/May/2021 11:48:39] "GET / HTTP/1.1" 200 -
API 요청 ID=9a8e5f1d-86c1-4304-a536-e5cb8ee072de
127.0.0.1 - - [10/May/2021 11:48:40] "GET / HTTP/1.1" 200 -
'''