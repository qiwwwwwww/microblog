from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    user ={ 'nickname': 'Emma'} # fake user
    posts =[ # fake array of posts
        {
            'author': { 'nickname' : 'Yang'},
            'body': ' I am so clever'
        },
        {
            'author': { 'nickname' : 'Liu'},
            'body': 'I am so stupid'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user =user,
                           posts = posts)

# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="'+ form.openid.data + '", remember_me='+ str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form =form,
                           providers = app.config['OPENID_PROVIDERS'])



# <html>
#    <head>
#      <title> Home Page </title>
#    </head>
#    <body>
#      <h1> Hello, ''' + user['nickname'] + ''' </h1>
#    </body>
# </html>
# '''
