from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
from db import getTaskList, addTask, updateTask, deleteTask

app = Flask(__name__)

# tasklist = [["Walk Dog", True], [
# "Wash Dishes", False], ["Take Out Trash", True]]


@app.route('/')
def index():
    tasklist = getTaskList()
    return render_template('index.html', TaskList=tasklist)


@app.route("/add", methods=['POST'])
def add():
    taskname = request.form['taskName']
    duedate = request.form['dueDate']
    addTask(taskname, duedate)
    return redirect(url_for('index'))


@app.route("/update", methods=['POST'])
def update():
    updatetaskname = request.form['updateTask']
    id = request.form['id']
    button = request.form['saveOrDelete']
    if button == "save":
        updateTask(updatetaskname, id)
    elif button == "X":
        deleteTask(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
