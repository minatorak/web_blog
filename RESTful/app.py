from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
    # curl -i http://localhost:5000/todo/api/v1.0/tasks
    # function generates for us from our data structure


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
        # return error page
    return jsonify({'task': task[0]})
    # curl -i http://localhost:5000/todo/api/v1.0/tasks/2
    # curl -i http://localhost:5000/todo/api/v1.0/tasks/3


@app.errorhandler(404)
def not_found(error):
    # make error page form line 33 to json error
    return make_response(jsonify({'error': 'Not found'}), 404)
    # curl -i http://localhost:5000/todo/api/v1.0/tasks/3


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    #POST method, which we will use to insert a new item in our task database:
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
    #curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=4995,debug=True)