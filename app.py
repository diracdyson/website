#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 03:48:00 2022

@author: brsantos
"""
from flask import Flask 
from views import views



app= Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.register_blueprint(views, url_prefix="/projects")
if __name__=='__main__':
    app.run(debug=True,port=8080)