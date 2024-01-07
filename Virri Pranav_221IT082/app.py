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
    if not request.json or 'task' not in request.json:
        return jsonify({'error': 'Invalid request'}), 400

    new_task = {
        'id': len(tasks) + 1,
        'task': request.json['task']
    }

    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Endpoint to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_to_delete = next((task for task in tasks if task['id'] == task_id), None)
    if task_to_delete:
        tasks.remove(task_to_delete)
        return jsonify({'result': 'Task deleted successfully'})
    else:
        return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
