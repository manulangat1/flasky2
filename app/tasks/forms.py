from flask_wtf import FlaskForm
from app.models import Task
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
#login form
class TaskForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    details = StringField('details',validators=[DataRequired()])
    submit = SubmitField('Submit')
#register form
