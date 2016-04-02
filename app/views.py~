from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user ={ 'nickname': 'Emma'} # fake user
    posts =[ #fake array of posts
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
# <html>
#    <head>
#      <title> Home Page </title>
#    </head>
#    <body>
#      <h1> Hello, ''' + user['nickname'] + ''' </h1>
#    </body>
# </html>
# '''
