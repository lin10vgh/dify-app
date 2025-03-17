import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    dify_url = os.getenv('DIFY_URL')  # Read the environment variable
    chat_app_name = os.getenv('CHAT_APP_NAME')
    return render_template('index.html', dify_url=dify_url, chat_app_name=chat_app_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

