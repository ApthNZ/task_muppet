#!/usr/bin/env python3

"""
Something I can throw tasks at
and then later maybe do them
starting with an API,
will do a web interface later
"""


from flask import Flask, jsonify, request


app = Flask(__name__)


# Instructions
@app.route('/')
def index():
    """Index route function"""
    return read_tasks()

# Task Creator
@app.route('/create')
def create():
    """Allow creation of task via query string"""
    description = request.args.get('description')
    status = 'Not Done'
    write_task(description, status)
    return "Task written to file\n"
    # TODO: Handle args being nothing

# File Manager
def write_task(description, status):
    """Append a new task to the tasks file"""
    with open('tasks.txt', 'a+') as file:
        task_json = jsonify({'description': description, 'status': status})
        file.write(task_json.get_data(as_text=True))
        # TODO: Put everything into one big JSON block, not separate blocks

def read_tasks():
    """Read all the tasks in the file"""
    with open('tasks.txt', 'r') as file:
        return ''.join(file.readlines())


# Run the app
if __name__ == '__main__':
    app.run()
