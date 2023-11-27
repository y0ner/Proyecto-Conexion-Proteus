from flask import Flask, jsonify, request, render_template
import crudSqlite as crud

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/sensor", methods=["GET"])
def get_sensor():
    sensor = crud.get_sensor()
    return jsonify(sensor)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)