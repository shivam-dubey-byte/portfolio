from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.route(/)
def __index__():
	return render_template('index.html')