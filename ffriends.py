from flask import Flask, render_template, request, redirect, session, url_for, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'Safe'
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
	query = 'SELECT * FROM friends'
	friends = mysql.query_db(query)
	return render_template('ffriends.html', friends=friends)

@app.route('/show/<id>')
def show(id):
	query = 'SELECT * FROM friends WHERE id = :id'
	data = { 'id': id }
	friend = mysql.query_db(query, data)
	return render_template('show.html', friendinfo=friend)

@app.route('/friends/<id>/edit')
def update(id):
	query = 'SELECT * FROM friends WHERE id=:id'
	data = { 'id': id }
	friend = mysql.query_db(query, data)
	return render_template('update.html', friendinfo=friend)

@app.route('/friends/<id>/edit', methods=['POST'])
def updateinfo(id):
	query = 'UPDATE friends SET name=:name, email=:email, updated_at=NOW() WHERE id=:id'
	data = { 'name':request.form['name'], 'email':request.form['email'], 'updated_at':request.form['update'], 'id':id }
	mysql.query_db(query, data)
	flash('Success!')
	return redirect('/')

@app.route('/friends', methods=['POST'])
def addinfo():
	query = 'INSERT INTO friends (id, name, email, created_at, updated_at) VALUES (DEFAULT, :name, :email, NOW(), NOW())'
	data = { 'name':request.form['name'], 'email':request.form['email'] }
	mysql.query_db(query, data)
	flash('Success!')
	return redirect('/')

@app.route('/friends')
def add():
	return render_template('add.html')

@app.route('/friends/<id>/delete')
def delete(id):
	query = 'DELETE FROM friends WHERE id = :id'
	data = { 'id': id}
	mysql.query_db(query, data)
	flash('Success!')
	return redirect('/')
app.run(debug=True)