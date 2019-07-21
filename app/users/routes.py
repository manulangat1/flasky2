from flask import request,Blueprint,url_for,render_template,redirect,flash
from flask_login import current_user,login_user,logout_user,login_required
from .forms import LoginForm,RegisterForm
from app.models import User
from app import db
from datetime import datetime
from app.models import User
#blueprint registration.
users = Blueprint('users',__name__)
#before request,records last time a user was in the
@users.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
#register route
@users.route('/register',methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('you have been succcessfully registered')
        return redirect(url_for('users.login'))
    return render_template('users/register.html',form=form,title="Register")
#login route
@users.route('/',methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invalid login details provided")
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('tasks.home')
        return redirect(next_page)
        # return redirect(url_for('tasks.home'))
    return render_template('users/login.html',form=form,title="Login")
#logout route
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))
