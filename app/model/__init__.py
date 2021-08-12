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
    return jsonify({'return':str(input)})

@app.route('/air',methods = ['get'])
def air():
    x1 = 1
    x2 = 2
    x3 = 3
    x4 = 4
    input = np.array([[x1,x2,x3,x4]])
    print(input)
    return jsonify({'return':str(input)})

if __name__  == "__main__":
    app.run(host = '0.0.0.0' , port = 3000 ,debug = True)