from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from utils import encode_message, decode_message
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash("No file uploaded!")
            return redirect(request.url)
        image = request.files['image']
        message = request.form['message']
        password = request.form['password']

        if not message or not password:
            flash("Message and password are required!")
            return redirect(request.url)

        if image.filename == '':
            flash("No selected file")
            return redirect(request.url)

        filename = secure_filename(image.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(path)

        output_path = os.path.join(UPLOAD_FOLDER, "encoded_" + filename)
        encode_message(path, message, password, output_path)

        flash("Message successfully encoded!")
        return send_file(output_path, as_attachment=True)

    return render_template('encode.html')

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash("No file uploaded!")
            return redirect(request.url)
        image = request.files['image']
        password = request.form['password']

        if image.filename == '':
            flash("No selected file")
            return redirect(request.url)

        filename = secure_filename(image.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(path)

        message = decode_message(path, password)
        return render_template('decode.html', decoded_message=message)

    return render_template('decode.html')

if __name__ == "__main__":
    app.run(debug=True)
