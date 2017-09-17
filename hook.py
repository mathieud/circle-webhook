from flask import Flask, request
import requests
app = Flask(__name__)

COLORS = {
    'success': 24173,
    'failed': 65423,
}

@app.route('/', methods=['GET', 'POST'])
def hook():
    print(request.get_json())
    print(request.get_json().get('read'))
    return 'OK'

    payload = request.get_json().get('payload', {})
    status = payload.get('status')
    failed = payload.get('failed')
    author = payload.get('author_email')

    requests.put('http://theodobridge.local:3000/hue/{}'.format(COLORS.get(status)))

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
