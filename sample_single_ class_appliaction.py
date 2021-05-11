# it is not working in this project since at the time of running we are specifying the flask app. 
# Hhence flask directly searches for that directory and the __init__ file inside it. 

# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

#defining a route
@app.route('/', methods = ['GET', 'PUT', 'POST'])
def home():
    # return "<html>\
    #             <body>\
    #                 <h3><u>Returning value from app file</u></h3>\
    #             </body>\
    #         </html>"
    return render_template('template.html')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/post', methods = ['POST'])
def sample_post_request():
    print(request.form['name'])
    # name = request.form['name']
    # age = request.form['age']
    # print ('name:', name, ' and age:', age)
    return 'worked'

#defining a route
@app.route('/abc', methods = ['GET', 'PUT', 'POST'])
def abc():
    return 'abc'

app.run(debug = True)
