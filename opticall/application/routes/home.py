#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        home
# @Date        2025-02-25 11:51:30
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from flask import Blueprint, render_template, redirect, url_for, request, flash

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    data = {}
    data['page_title'] = 'Inicio'
    return render_template('home/index.html', data=data)

