from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/privacy/cookies.html')
def cookies_policy():
    # Sirve el archivo cookies.html desde la carpeta privacy
    return send_from_directory(os.path.join(app.root_path, 'privacy'), 'cookies.html')

if __name__ == "__main__":
    app.run(debug=True)
