from flask import Blueprint, render_template
from . import celery

bp = Blueprint('views', __name__)

@bp.route('/')
def home():
    message = 'Welcome to DocMaker!'
    return render_template('home.html', message=message)

@bp.route('/start_task', methods=['POST'])
def start_task():
    task = long_running_task.delay()
    return task, task_id

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


@celery.task(bind=True)
def long_running_task(self):
    # long running task here
    pass
