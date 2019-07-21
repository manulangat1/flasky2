from flask import Blueprint,url_for,redirect,render_template,flash
from app.models import Task
from flask_login import login_required
from .forms import TaskForm
from app import db
#blueprint initialisation
tasks = Blueprint('tasks',__name__)

#home page
@tasks.route('/tasks',methods=["GET","POST"])
@login_required
def home():
    tas = Task.query.all()
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(name=form.name.data,details=form.details.data)
        db.session.add(task)
        db.session.commit()
        flash("added succcessfully")
        return redirect(url_for('tasks.home'))
    return render_template('tasks/home.html',title="home",form=form,tas=tas)
