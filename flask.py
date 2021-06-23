from flask import Flask, render_template, jsonify
import test
import main
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        main.start()

    return render_template('index.html')