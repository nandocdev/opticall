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

shifts_bp = Blueprint('shifts', __name__)

@shifts_bp.route('/')
def home():
    data = {}
    data['page_title'] = 'Gestión de turnos'
    return render_template('shifts/shifts.html' , data=data)

@shifts_bp.route('/calendar')
def calendar():
    data = {}
    data['page_title'] = 'Calendario de turnos'
    return render_template('shifts/calendar.html', data=data)

@shifts_bp.route('/request')
def request_shift():
    data = {}
    data['page_title'] = 'Solicitar cambio de turno'
    return render_template('shifts/request_shift.html', data=data)

@shifts_bp.route('/approve')
def approve():
    data = {}
    data['page_title'] = 'Aprobar o rechazar cambios de turno'
    return render_template('shifts/approve.html', data=data)

@shifts_bp.route('/history')
def shift_history():
    data = {}
    data['page_title'] = 'Historial de turnos'
    return render_template('shifts/shift_history.html', data=data)