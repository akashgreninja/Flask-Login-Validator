
from flask import Flask, render_template
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField,PasswordField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

# use this docs
# https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/

app = Flask(__name__)

Bootstrap(app)
app.secret_key = "akash13"
class LoginForm(FlaskForm):
    email= StringField(label='Email' ,validators=[DataRequired()])
    password= PasswordField(label='password',validators=[DataRequired()])
    submit=SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')

string_1=["admin@email.com","12345678"]
@app.route("/login",methods=["GET","POST"])
def login():
   
    form = LoginForm()
    if form.validate_on_submit():
        if string_1[0]==form.email.data and string_1[1]==form.password.data:
            return render_template("success.html")
        else:
            return render_template("denied.html")    

    
   
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)