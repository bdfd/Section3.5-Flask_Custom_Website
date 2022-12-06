'''
Date         : 2022-12-05 14:13:08
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-12-05 14:28:08
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
def index():
  return render_template('index.html')

@app.route('/home')
def home():
  return 'Hello! this is the main page.'

@app.route('/<name>')
def user(name):
  return f'Hello {name}'

@app.route('/admin')
def admin():
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)
