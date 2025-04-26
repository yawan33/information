from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# 记录已注册的人数
registered_users = 0

@app.route('/')
def index():
    return render_template('index.html', registered_users=registered_users)

@app.route('/register', methods=['POST'])
def register():
    global registered_users
    name = request.form['name']
    registered_users += 1
    return redirect(url_for('success', name=name))

@app.route('/success')
def success():
    return render_template('success.html', name=request.args['name'])

if __name__ == '__main__':
    app.run(debug=True)
