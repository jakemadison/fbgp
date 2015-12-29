#! /usr/bin/env python

__author__ = 'Madison'

from app import app

app.run(debug=True,
        # host='0.0.0.0',  # do you trust everyone on the local network?
        port=5050)
