from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data structure to store tasks
tasks = []

# Endpoint to get the list of tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Endpoint to add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {'task': data['task']}
    tasks.append(new_task)
    return jsonify({'message': 'Task added successfully'})

# Endpoint to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        return jsonify({'message': 'Task deleted successfully', 'deleted_task': deleted_task})
    else:
        return jsonify({'error': 'Invalid task ID'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)

