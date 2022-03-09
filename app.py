from urllib import request
from flask import Flask, render_template, redirect, request

from tasks import factorial

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/create_task_factorial')
def create_task_factorial():
    n = int(request.args.get('n', 0))
    task = factorial.delay(n)
    return redirect('/')
