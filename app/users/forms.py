from flask_wtf import FlaskForm
from app.models import User
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
#login form
class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')
#register form
class RegisterForm(FlaskForm):
    username  = StringField('username',validators=[DataRequired()])
    email  = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    password2 = PasswordField('password2',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')
    #validate the username
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username exists use a different one')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email exists use a different one')
