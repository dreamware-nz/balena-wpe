from flask import Flask, escape, request, render_template, jsonify
import datetime

KIOSK_VERSION = "1.0.9"
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return render_template('hello.html', name=name, kiosk_version=KIOSK_VERSION)

@app.route('/version')
def version():
    return jsonify({'version': KIOSK_VERSION, 'datetime': datetime.datetime.now().isoformat()})
