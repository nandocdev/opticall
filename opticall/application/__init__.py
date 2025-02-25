#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     OptiCall/opticall
# @subpackage  application
# @file        __init__
# @Date        2025-02-25 11:44:24
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from flask import Flask
from opticall.application.routes import register_blueprints

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
register_blueprints(app)


