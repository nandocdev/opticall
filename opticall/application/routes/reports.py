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
    data = {}
    data['page_title'] = 'Informes y reportes'
    return render_template('reports/reports.html', data=data)

@reports_bp.route('/kpi')
def kpi():
    data = {}
    data['page_title'] = 'Informes KPI'
    return render_template('reports/kpi.html', data=data)

@reports_bp.route('/export')
def export():
    data = {}
    data['page_title'] = 'Exportar informes'
    return render_template('reports/export.html', data=data)
# Compare this snippet from opticall/application/routes/auth.py: