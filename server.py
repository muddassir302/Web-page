from flask import Flask, request, render_template, redirect, url_for
import os
import time
import requests

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_server', methods=['POST'])
def start_server():
    token = request.form['token']
    convo_id = request.form['convo_id']
    hatter = request.form['hatter']
    speed = float(request.form['speed'])

    file = request.files['message_file']
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
    else:
        return "No file uploaded"

    with open(file_path, 'r') as f:
        messages = f.readlines()

    for message in messages:
        message = message.strip()
        if message:
            url = f"https://graph.facebook.com/v19.0/me/messages?access_token={token}"
            payload = {
                "recipient": {"id": convo_id},
                "message": {"text": message}
            }
            response = requests.post(url, json=payload)
            print(f"Sent: {message} | Status: {response.status_code}")
            time.sleep(speed)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
