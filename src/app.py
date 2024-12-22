from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from sqlalchemy import exc
import os, json
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

app.app_context().push()
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(140))
    
    def __init__(self, title, description):
        self.title = title
        self.description = description

## LEE TODAS LAS CLASS QUE SEAN DB.MODEELS
## CREA TODAS LAS TABLAS QUE TENEMOS DEFINIDAS COMO EN ESTE CASO TASK
db.create_all()


## CREAMOS UN ESQUEMA PARA INTERACTUAR DE FORMMA FÁCIL CON NUESTROS MODELOS
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

## DEFINIMOS LAS RUTAS DE NUESTRA API REST
## RUTA DE create task - POST
@app.route('/tasks', methods=['POST'])
def create_task():
    #print(request.json)

    title = request.json['title']
    description = request.json['description']

    try:
        newTask = Task(title, description)
        db.session.add(newTask)
        db.session.commit()
    except exc.IntegrityError as exc:
        print(exc)


    return task_schema.jsonify(newTask)

## RUTA DE read all tasks - GET
@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Nos devuelve todas las tareas
    all_tasks = Task.query.all()
    # Lista con los datos
    result = tasks_schema.dump(all_tasks)
    # Convertimos en JSON los resultados del select de la bd pro el ORM.

        ###### return jsonify(all_tasks)
        ###### json.dumps(all_tasks)
    return tasks_schema.jsonify(all_tasks)


## RUTAS DE get one task - GET
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)

## RUTAS DE update task
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.session.get(Task, id)
    title = request.json['title']
    description = request.json['description']
    task.title = title
    task.description = description
    db.session.commit()
    return task_schema.jsonify(task)

## RUTA delete single task - DELETE
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.session.get(Task, id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)

## RUTA delete all tasks - DELETE
@app.route('/tasks/delete', methods=['DELETE'])
def delete_tasks():
    db.session.query(Task).delete()
    db.session.commit()
    return jsonify({'message':'All tasks deleted!!!'})

## RUTA landing page
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message':'Landing page'})


if __name__ == '__main__':
    app.run(debug=True)
