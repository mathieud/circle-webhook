from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hook(request):
    print(request.data)
    return "Hello World!"
