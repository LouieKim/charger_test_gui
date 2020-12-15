from flask import Flask, render_template, jsonify
import serial

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/door/<command>')
def door(command):
    print("%s" %command)
    SER = serial.Serial('COM-7', 115200)
    SER.write('a')
    return jsonify(success=True)

def main():
    app.run(host="127.0.0.1", port="5000", debug=True)

if __name__ == "__main__":
    main()