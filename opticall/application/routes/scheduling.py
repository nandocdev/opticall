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

schedule = Blueprint('schedule', __name__)


@schedule.route('/')
def home():
    return render_template('scheduling/scheduling.html')


@schedule.route('/rules')
def rules():
    return render_template('scheduling/rules.html')


@schedule.route('/generate')
def generate():
    return render_template('scheduling/generate.html')


@schedule.route('/results')
def results():
    schedule_data = {}
    return render_template('scheduling/results.html', schedule_data=schedule_data)


@schedule.route('/logs')
def logs():
    return render_template('scheduling/logs.html')
