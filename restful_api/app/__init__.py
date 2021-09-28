from flask import Flask , request , jsonify
from werkzeug.exceptions import RequestTimeout
from flask_cors import CORS
from flask import abort


app = Flask(__name__)
CORS(app)

#restful-api

# CREATE   - POST
# READ ALL - GET
# READ ONE - GET
# UPDATE   - PUT
# DELETE   - DELETE

data = [
    {'id':1,
    'title':'title1',
    'data':'data1'
    },
    {'id':2,
    'title':'title2',
    'data':'data2'
    },
    {'id':3,
    'title':'title3',
    'data':'data3'
    }
]

@app.route('/restful_task/',methods = ['GET'])
def get_task():
    return jsonify({'task':data}) , 201


@app.route('/restful_task/<int:task_id>',methods = ['GET'])
def get_task1(task_id):
    task = [ i for i in data if i['id']==task_id]
    if len(task)> 0 :
        return jsonify({'task':task}) , 201
    else :
        return abort(404)


@app.route('/restful_task/',methods = ['POST'])
def post_task():
    if request.json is None or 'title' not in request.json:
        return abort(400)
    else :
        task = {
        'id':data[-1]['id'] + 1,
        'title':request.json['title'],
        'data':request.json.get('data','null')# 如果沒給就填入null
        }
        data.append(task)
        return jsonify({'post success':task}) ,201

@app.route('/restful_task/<int:task_id>',methods=['PUT'])
def updata_task(task_id):
    if request.json is None:
        return abort(400 , "No json data")
    else:
        if len(str(request.json['title']))<1:
            return abort(400 , "No title")
        if  type(request.json['title'])!=str:
            return abort(400 , "type error")
        if task_id not in [i['id'] for i in data]:
            return jsonify({'result':f'id{task_id}is empty'} , 400)

    task = [i for i in data if i['id']==task_id]
    task[0]['title'] = request.json.get('title',task[0]['title'])
    task[0]['data'] = request.json.get('data',task[0]['data'])
    return jsonify({f'update pass {task_id}':True})


@app.route('/restful_task/<int:task_id>',methods = ['DELETE'])
def delete_task(task_id):
    if len(data)<=0:
        return jsonify({'result':'DB is null'})

    if task_id in [i['id'] for i in data]:
        task = [i for i in data if i['id']==task_id]
        data.remove(task[0])
        return jsonify({'delete_finish':True})
    else :
        return jsonify({'delete_fail':f'there is no id = {task_id}'})