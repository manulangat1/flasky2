from flask import Blueprint,url_for,redirect,request,jsonify
from app.models import User,Task
from app import db,ma
# from .forms import TaskForm
from .schema import TaskSchema

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id','name','details','posted')
#init the schema
task_schema = TaskSchema(strict=True)
tasks_schema = TaskSchema(strict=True,many=True)
#create your routes here.
api = Blueprint('api',__name__)
#create your routes here.
@api.route('/api',methods=["GET","POST"])
def get():
    tasks = Task.query.all()
    result = tasks_schema.dump(tasks)
    return jsonify(result.data)
@api.route('/task',methods=["POST"])
def add_task():
    name = request.json['name']
    details = request.json['details']
    newTask = Task(name=name,details=details)
    db.session.add(newTask)
    db.session.commit()
    return task_schema.jsonify(newTask)
#get single task
@api.route('/api/<id>',methods=["GET","POST"])
def get_task(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)
#update task
@api.route('/task/<id>',methods=["PUT"])
def update_task(id):
    task = Task.query.get(id)
    name = request.json['name']
    details = request.json['details']
    task.name = name
    task.details = details
    db.session.commit()
    return task_schema.jsonify(task)
#delete task
@api.route('/api/<id>',methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)
