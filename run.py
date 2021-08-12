from flask import Flask , request , jsonify
from flask_cors import CORS
import numpy as  np

app = Flask(__name__)
CORS(app)

@app.route('/flower',methods = ['POST'])
def flower():
    insert_value = request.get_json()
    x1 = insert_value['length']
    x2 = insert_value['heigh']

    input = np.array([[x1,x2]])
    print(input)

    return jsonify({'return':'get_data'})

@app.route('/air',methods = ['POST'])
def air():
    insert_value = request.get_json()
    x1 = insert_value['deg_c']
    x2 = insert_value['sensor_1']
    x3 = insert_value['sensor_2']
    x4 = insert_value['sensor_3']

    input = np.array([[x1,x2,x3,x4]])
    print(input)

    return jsonify({'return':'get_data'})


if __name__  == "__main__":
    app.run(host = '0.0.0.0' , port = 3000 ,debug = True)