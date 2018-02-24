from flask import Flask, jsonify, abort

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
    # curl -i http://localhost:5000/todo/api/v1.0/tasks
    # function generates for us from our data structure
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # curl -i http://localhost:5000/todo/api/v1.0/tasks/2
    # curl -i http://localhost:5000/todo/api/v1.0/tasks/3
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
        # return error page
    return jsonify({'task': task[0]})

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=4995,debug=True)