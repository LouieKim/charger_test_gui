from flask import Flask, render_template, jsonify
import serial

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/door/<command>')
def door(command):
    
    try:
        SER = serial.Serial('COM7', 115200)
        if(command == 'on'):
            print("%s" %command)
            SER.write(b'a')
        elif(command == 'off'):
            print("%s" %command)
            SER.write(b'a')
        else:
            print("Error")
    except Exception as e:
        print(e)
    finally:
        SER.close()

    return jsonify(success=True)

def main():
    app.run(host="127.0.0.1", port="5000", debug=True)

if __name__ == "__main__":
    main()