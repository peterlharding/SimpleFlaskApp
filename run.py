#!/usr/bin/env python

from flaskapp import app as application

print("Yes...")

if __name__ == '__main__':
    application.run(host='127.0.0.1', port=8088)

