#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        monitoring
# @Date        2025-02-25 11:04:11
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Rutas que generan vistas de monitoreo en tiempo real
"""
    ## **📡 monitoring.py** (Monitoreo en tiempo real)
    | Método | Ruta | Descripción |
    |--------|------|-------------|
    | `GET`  | `/monitoring` | Panel de control en tiempo real |
    | `GET`  | `/monitoring/alerts` | Configuración de alertas |
    | `GET`  | `/monitoring/agents` | Estado en tiempo real de los agentes |
    | `GET`  | `/monitoring/summary` | Resumen de estadísticas |
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash

monitoring_bp = Blueprint('monitoring', __name__)

@monitoring_bp.route('/')
def home():
    data = {}
    data['page_title'] = 'Monitoreo en tiempo real'
    return render_template('monitoring/monitoring.html', data=data)

@monitoring_bp.route('alerts')
def alerts():
    data = {}
    data['page_title'] = 'Alertas'
    return render_template('monitoring/alerts.html', data=data)

@monitoring_bp.route('/agents')
def agents():
    data = {}
    data['page_title'] = 'Estado de Agentes'
    return render_template('monitoring/agents.html', data=data)

@monitoring_bp.route('/summary')
def summary(): 
    data = {}
    data['page_title'] = 'Resumen de estadísticas'
    return render_template('monitoring/summary.html', data=data)
