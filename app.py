from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_task():
    token_option = request.form.get('token_option')
    single_token = request.form.get('single_token')
    inbox_uid = request.form.get('inbox_uid')
    hater_name = request.form.get('hater_name')
    time_seconds = request.form.get('time_seconds')
    file = request.files.get('np_file')

    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    # Yahan tum convo chalane wali script laga sakte ho ya dummy response dena hai
    print(f"Running task: Token: {single_token}, Inbox: {inbox_uid}, Hater: {hater_name}, Time: {time_seconds}")

    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop_task():
    task_id = request.form.get('task_id')
    print(f"Stopping task: {task_id}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
