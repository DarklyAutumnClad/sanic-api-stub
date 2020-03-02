#!/usr/bin/env python3.7
from sanic import Sanic
from sanic import response
import json


app = Sanic(__name__)
pinned = json.dumps({
    "SomeElement": "SomeValue",
    "SomeArrayName": [
        "arrayvalue1",
        "arrayvalue2"
        ]
    })

@app.route('/api/V2/multimethodexample', methods=["POST", "GET"])
async def multimethodexample(request):
    return response.text(pinned, status=200, headers=None,
                         content_type='application/json')

@app.route('/api/V2/HealthCheck/', methods=["GET"])
async def HealthCheck(request):
    return response.text('true', status=200, headers=None,
                         content_type='text/html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
