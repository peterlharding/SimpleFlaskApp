#!/usr/bin/env python
#
#--------------------------------------------------------------------------

import sys

from datetime import datetime

#--------------------------------------------------------------------------

from flask import render_template, flash, redirect, session, url_for, request, g

#--------------------------------------------------------------------------

from . import app, db

from .context import Context
from .trace   import Trace

from .models import User, ROLE_USER, ROLE_ADMIN

#--------------------------------------------------------------------------

@app.route('/')
def home():

    ctx = Context('Home')

    return render_template("index.html", ctx=ctx)

#--------------------------------------------------------------------------

@app.route('/contactus-01')
def contactus_01():

    ctx = Context('About')

    return render_template("contactus_01.html", ctx=ctx)

#--------------------------------------------------------------------------

@app.route('/contactus-02')
def contactus_02():

    ctx = Context('About')

    return render_template("contactus_02.html", ctx=ctx)

#--------------------------------------------------------------------------

@app.route('/about')
def about():

    ctx = Context('About')

    return render_template("about.html", ctx=ctx)

#--------------------------------------------------------------------------

if __name__ == '__main__':
    app.run()

#--------------------------------------------------------------------------

