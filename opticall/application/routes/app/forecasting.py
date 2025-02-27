#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        forecasting
# @Date        2025-02-25 11:01:11
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Rutas que generan vistas de pronóstico de llamadas
"""
    ## **📊 forecasting.py** (Pronóstico)
    | Método | Ruta | Descripción |
    |--------|------|-------------|
    | `GET`  | `/forecast` | Página principal del módulo de pronóstico |
    | `GET`  | `/forecast/upload` | Subir datos históricos para generar pronósticos |
    | `GET`  | `/forecast/results` | Visualizar los pronósticos generados |
    | `GET`  | `/forecast/configure` | Configurar parámetros del modelo de pronóstico |
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash

forecasting_bp = Blueprint('forecasting', __name__)

@forecasting_bp.route('/')
def forecast():
    data = {}
    data['page_title'] = 'Pronóstico de llamadas'
    return render_template('forecasting/forecast.html', data=data)

@forecasting_bp.route('/upload')
def upload():
    data = {}
    data['page_title'] = 'Carga de archivos '
    return render_template('forecasting/upload.html', data=data)

@forecasting_bp.route('/results')
def results():
    data = {}
    data['page_title'] = 'Resultados'
    return render_template('forecasting/results.html', data=data)

@forecasting_bp.route('/configure')
def configure():
    data = {}
    data['page_title'] = 'Configuración'
    return render_template('forecasting/configure.html', data=data)


    