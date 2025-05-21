from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_task():
    token_option = request.form['token_option']
    single_token = request.form['single_token']
    convo_uid = request.form['convo_uid']
    hater_name = request.form['hater_name']
    time_seconds = request.form['time_seconds']

    file = request.files['np_file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

    print("Token Option:", token_option)
    print("Single Token:", single_token)
    print("Convo UID:", convo_uid)
    print("Hater Name:", hater_name)
    print("Time (seconds):", time_seconds)
    print("File saved at:", filepath if file else "No file")

    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop_task():
    task_id = request.form['task_id']
    print("Task stopped:", task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
