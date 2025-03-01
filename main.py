import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ensure upload folder exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return '''
    <html>
        <body>
            <h1>WhatsApp Message Automation</h1>
            <form action="/send" method="POST" enctype="multipart/form-data">
                <label for="target_number">Target Phone Number:</label><br>
                <input type="text" id="target_number" name="target_number" required><br><br>

                <label for="message_file">Message File:</label><br>
                <input type="file" id="message_file" name="message_file" required><br><br>

                <label for="hater_name">Hater Name:</label><br>
                <input type="text" id="hater_name" name="hater_name" required><br><br>

                <label for="delay">Message Delay (seconds):</label><br>
                <input type="number" id="delay" name="delay" required><br><br>

                <button type="submit">Start Automation</button>
            </form>
        </body>
    </html>
    '''

@app.route('/send', methods=['POST'])
def send():
    target_number = request.form['target_number']
    message_file = request.files['message_file']
    hater_name = request.form['hater_name']
    delay = request.form['delay']
    
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, message_file.filename)
    message_file.save(file_path)

    # Run the WhatsApp automation script with the parameters
    subprocess.Popen(['node', 'whatsapp_automation_script.js', target_number, file_path, hater_name, delay])
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
