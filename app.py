from urllib import request
from flask import Flask, render_template, redirect, request, url_for

from tasks import factorial

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/factorial/')
def create_task_factorial():
    n = int(request.args.get('n', 0))
    task = factorial.delay(n)
    return redirect(url_for('check_task_status', task_id=task.task_id))


@app.route('/status/<string:task_id>/')
def check_task_status(task_id):
    result = factorial.AsyncResult(task_id)
    return render_template('status.html', result=result)

