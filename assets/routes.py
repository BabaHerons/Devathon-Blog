from assets import app

@app.route('/')
def home():
    return 'Hey I am working.'