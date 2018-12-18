#!/usr/bin/env python

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#--------------------------------------------------------------------------

import appconfig

from appconfig import ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

#--------------------------------------------------------------------------

basedir = os.path.abspath(os.path.dirname(__file__))

#--------------------------------------------------------------------------

app = Flask(__name__)

app.config['DEBUG'] = True

app.config.from_object('appconfig')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

db = SQLAlchemy(app)

#--------------------------------------------------------------------------

from . import routes

#--------------------------------------------------------------------------

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

#--------------------------------------------------------------------------

