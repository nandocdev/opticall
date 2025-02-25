#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        reports
# @Date        2025-02-25 11:06:22
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Rutas que generan vistas de informes y reportes
"""
    ## **📈 reports.py** (Informes)
    | Método | Ruta | Descripción |
    |--------|------|-------------|
    | `GET`  | `/reports` | Página principal de informes |
    | `GET`  | `/reports/kpi` | Informes de KPIs (AHT, FCR, NPS) |
    | `GET`  | `/reports/export` | Exportar informes en PDF/Excel |
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/')
def home():
    return render_template('reports/reports.html')

@reports_bp.route('/kpi')
def kpi():
    return render_template('reports/kpi.html')

@reports_bp.route('/export')
def export():
    return render_template('reports/export.html')
# Compare this snippet from opticall/application/routes/auth.py: