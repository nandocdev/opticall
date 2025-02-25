#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        scheduling
# @Date        2025-02-25 11:07:54
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Rutas que generan vistas de planificación y monitoreo de llamadas
"""
    ## **📅 scheduling.py** (Planificación)
    | Método | Ruta | Descripción |
    |--------|------|-------------|
    | `GET`  | `/scheduling` | Página principal de la planificación |
    | `GET`  | `/scheduling/rules` | Configuración de reglas de planificación |
    | `GET`  | `/scheduling/generate` | Generar un nuevo horario de trabajo |
    | `GET`  | `/scheduling/results` | Vista de horarios generados |
    | `GET`  | `/scheduling/logs` | Visualizar los registros de planificación |
"""

import sched
from flask import Blueprint, render_template, redirect, url_for, request, flash

scheduling_bp = Blueprint('schedule', __name__)


@scheduling_bp.route('/')
def home():
    data = {}
    data['page_title'] = 'Planificación de llamadas'
    return render_template('scheduling/scheduling.html', data=data)


@scheduling_bp.route('/rules')
def rules():
    data = {}
    data['page_title'] = 'Configuración de reglas'
    return render_template('scheduling/rules.html', data=data)


@scheduling_bp.route('/generate')
def generate():
    data = {}
    data['page_title'] = 'Generar horario de trabajo'
    return render_template('scheduling/generate.html', data=data)


@scheduling_bp.route('/results')
def results():
    
    data = {}
    data['page_title'] = 'Resultados de horarios generados'
    return render_template('scheduling/results.html', data=data)


@scheduling_bp.route('/logs')
def logs():
    data = {}
    data['page_title'] = 'Registros de planificación'
    return render_template('scheduling/logs.html', data=data)
