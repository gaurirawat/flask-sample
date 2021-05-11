from flask import render_template, jsonify

from app import app

@app.route('/')
def template_function():
    return render_template("index.html")


@app.route('/about')
def non_template_function():
    return 'about: Return value without rendering template'

@app.route('/<int:number>/')
def number_query_parameter(number):
    return "number is " + str(number)

@app.route('/name/<string:name>/')
def string_query_parameter(name):
    return "Hello " + name

@app.route('/json')
def json():
    return jsonify({'name':'Jimit',
                    'address':'India'})