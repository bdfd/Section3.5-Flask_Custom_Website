'''
Author: BDFD
Date: 2022-02-03 15:32:30
LastEditTime: 2022-06-20 13:56:37
LastEditors: BDFD
Description: 
FilePath: \Section3.5-Flask_Custom_Website\server.py
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



if __name__ == '__main__':
  app.run(debug=True)
