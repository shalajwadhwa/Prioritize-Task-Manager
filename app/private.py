from app import app
from app.models import db, User, Tasks
from flask import render_template, request, redirect
from flask_login import login_required, current_user, logout_user
from werkzeug.security import generate_password_hash


@app.route('/matrix')
@login_required
def matrix():
    do = Tasks.query.filter_by(user_id=current_user.id, imp=1, urg=1)
    schedule = Tasks.query.filter_by(user_id=current_user.id, imp=1, urg=0)
    delegate = Tasks.query.filter_by(user_id=current_user.id, imp=0, urg=1)
    avoid = Tasks.query.filter_by(user_id=current_user.id, imp=0, urg=0)
    return render_template('private/matrix.html', title='Matrix', matrix='active', do=do, schedule=schedule, delegate=delegate, avoid=avoid, profile_picture=current_user.name)

@app.route('/all_tasks')
@login_required
def all_tasks():
    data = Tasks.query.filter_by(user_id=current_user.id)
    return render_template('private/all_tasks.html', title='All Tasks', table='active', data=data, profile_picture=current_user.name)

@app.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        name, desc, imp, urg = request.form.get('name'), request.form.get('desc'), request.form.get('imp'), request.form.get('urg')
        if imp : imp=int(imp)
        if urg : urg=int(urg)
        task = Tasks(task=name, user_id=current_user.id, desc=desc, imp=imp, urg=urg)
        db.session.add(task)
        db.session.commit()
    return render_template('private/add_task.html', title='Add Task', action='Add Task', add='active', profile_picture=current_user.name)

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Tasks.query.filter_by(id=task_id, user_id=current_user.id).first()
    if request.method == 'GET':
        if task != None:
            imp='checked' if task.imp!=0 else 0
            urg='checked' if task.urg!=0 else 0
            return render_template('private/add_task.html', title='Edit Task', action='Update Task', name=task.task, desc=task.desc, check_imp=imp, check_urg=urg, profile_picture=current_user.name)
        return {'Error': 'Invalid Task'}
    name, desc, imp, urg = request.form.get('name'), request.form.get('desc'), request.form.get('imp'), request.form.get('urg')
    imp = 1 if imp!=None else 0
    urg = 1 if urg!=None else 0
    task.task, task.desc, task.imp, task.urg = name, desc, imp, urg
    db.session.commit()
    return redirect('/all_tasks')

@app.route('/delete_task/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Tasks.query.filter_by(id=task_id, user_id=current_user.id).first()
    if task == None:
        return {'Error': 'Invalid Task'}
    db.session.delete(task)
    db.session.commit()
    return redirect('/all_tasks')

@app.route('/complete_task/<int:task_id>')
@login_required
def complete_task(task_id):
    task = Tasks.query.filter_by(id=task_id, user_id=current_user.id).first()
    if task == None:
        return {'Error': 'Invalid Task'}
    db.session.delete(task)
    db.session.commit()
    return redirect('/matrix')

@app.route('/profile')
@login_required
def profile():
    return render_template('private/profile.html', title='Profile', name=current_user.name, email=current_user.email, profile_picture=current_user.name)

@app.route('/reset_password', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        password = request.form.get('password')
        user = User.query.filter_by(id=current_user.id).first()
        user.password_hash = generate_password_hash(password)
        db.session.commit()
        logout_user()
        return redirect('/login')
    return render_template('private/reset_password.html', title='Edit Profile', profile_picture=current_user.name, name=current_user.name)

