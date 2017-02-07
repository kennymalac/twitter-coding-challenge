# -*- coding: utf-8 -*-
"""
    Globus Challenge

"""

from flask import Flask, g, render_template
from app import *
import api


@app.route('/')
def challenge():
    return render_template('main.html')

