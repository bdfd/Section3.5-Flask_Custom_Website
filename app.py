'''
Date         : 2022-12-05 14:13:08
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-12-07 18:04:59
LastEditors  : BDFD
Description  : 
FilePath     : \app.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
# from crypt import methods
# from pickle import TRUE
# from unittest import result
# from uuid import RESERVED_FUTURE
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
  if request.method == 'POST':
    session.permanent = True
    user = request.form['nm']
    session['user'] = user
    return redirect(url_for('user'))
  else:
    if 'user' in session:
      return redirect(url_for('user'))
    return render_template('login.html')

@app.route('/user')
def user():
  if 'user' in session:
    user = session['user']
    print(user)
    return f'<h1>{user}</h1>'
  else:
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
  session.pop('user', None)
  return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(debug=True)
