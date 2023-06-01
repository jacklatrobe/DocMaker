from flask import Blueprint, render_template
import logging
from . import celery

bp = Blueprint('views', __name__)

# Define the home route
@bp.route('/')
def home():
    message = 'Welcome to DocMaker!'
    logging.info('Rendering home page')
    return render_template('home.html', message=message)

# Define the route to start async AI task
@bp.route('/start_task', methods=['POST'])
def start_task():
    try:
        task = long_running_task.delay()
        return task, task_id
    except Exception as e:
        return str(e), 500

# Define the route to check async AI task
@bp.route('/task_status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = celery.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Task is pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'status': str(task.info),  # this is the result of the task
        }
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
