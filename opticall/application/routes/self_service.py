#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        self_service
# @Date        2025-02-25 11:11:52
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Rutas que generan vistas de autoservicio de usuarios internos
"""
    ## **👨‍💻 self_service.py** (Portal de Autoservicio para Empleados)
    | Método | Ruta | Descripción |
    |--------|------|-------------|
    | `GET`  | `/self-service` | Página de inicio del portal de empleados |
    | `GET`  | `/self-service/schedule` | Ver horario personal |
    | `GET`  | `/self-service/request-shift` | Solicitar cambio de turno |
    | `GET`  | `/self-service/info` | Información relevante para empleados |
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash

self_service = Blueprint('self_service', __name__)

@self_service.route('/')
def home():
    return render_template('self_service/self_service.html')

@self_service.route('/schedule')
def schedule():
    return render_template('self_service/schedule.html')

@self_service.route('/request-shift')
def request_shift():
    return render_template('self_service/request_shift.html')

@self_service.route('/info')
def info():
    return render_template('self_service/info.html')
# Compare this snippet from opticall/application/routes/admin.py:
