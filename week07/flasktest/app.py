from flask import Flask, request, escape, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html.jinja2', username="Nat")
"""@app.route('/')
def index():
	return '%s' % "Hello"""
"""@app.route('/', methods=['GET', 'POST'])
def index():
	return jsonify({'method' : request.method})"""
"""@app.route('/')
def index():
	a = escape(request.args.get('a'))
	return f'a = {a}'"""
"""
@app.route('/')
def index():
	return jsonify({'a' : 1})"""

"""@app.route('/')
def index():
    return 'Hello, World! This is /'

@app.route('/hello/<username>')
def hello(username):
	return f'Hello, {username}'

@app.route('/increment/<int:value>')
def increment(value):
	value += 1
	return f'Result: {value}'"""

