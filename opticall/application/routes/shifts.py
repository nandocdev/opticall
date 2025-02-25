#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        shifts
# @Date        2025-02-25 11:13:10
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Rutas que generan vistas de turnos y horarios
"""
    ## **🕒 shifts.py** (Gestión de Turnos)
    | Método | Ruta | Descripción |
    |--------|------|-------------|
    | `GET`  | `/shifts` | Página principal de turnos |
    | `GET`  | `/shifts/calendar` | Visualización de turnos en formato de calendario |
    | `GET`  | `/shifts/request` | Solicitar cambio de turno |
    | `GET`  | `/shifts/approve` | Aprobar o rechazar cambios de turno |
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash

shifts = Blueprint('shifts', __name__)

@shifts.route('/')
def home():
    return render_template('shifts/shifts.html')

@shifts.route('/calendar')
def calendar():
    return render_template('shifts/calendar.html')

@shifts.route('/request')
def request_shift():
    return render_template('shifts/request_shift.html')

@shifts.route('/approve')
def approve():
    return render_template('shifts/approve.html')
# Compare this snippet from opticall/application/routes/monitoring.py: