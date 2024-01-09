Create a virtual environment: python -m venv venv

Activate the virtual environment: \venv\Scripts\Activate

Install dependencies: pip install -r requirements.txt

Run the Flask application: python app.py

Get the list of tasks: curl http://127.0.0.1:5000/tasks

Add a new task: curl -X POST -H "Content-Type: application/json" -d '{"title":"Your Task Title"}' http://127.0.0.1:5000/tasks

Delete a task (replace <task_id> with the actual task ID): curl -X DELETE http://127.0.0.1:5000/tasks/<task_id>
