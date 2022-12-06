'''
Date         : 2022-12-05 14:13:08
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-12-06 13:38:06
LastEditors  : BDFD
Description  : 
FilePath     : \app.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
# from crypt import methods
# from pickle import TRUE
# from unittest import result
# from uuid import RESERVED_FUTURE
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
  if request.method == 'POST':
    user = request.form['nm']
    print(user)
    return redirect(url_for('user', usr=user))
  else:
    return render_template('login.html')

@app.route('/<usr>')
def user(usr):
  return f'<h1>{usr}</h1>'

if __name__ == '__main__':
  app.run(debug=True)
