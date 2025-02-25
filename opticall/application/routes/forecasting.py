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
    return render_template('forecasting/.html')

@forecasting_bp.route('/upload')
def upload():
    return render_template('forecasting/upload.html')

@forecasting_bp.route('/results')
def results():
    forecast_data = {}
    return render_template('forecasting/results.html', forecast_data=forecast_data)

@forecasting_bp.route('/configure')
def configure():
    return render_template('forecasting/configure.html')


    