#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     OptiCall/opticall
# @subpackage  application
# @file        __init__
# @Date        2025-02-25 12:04:16
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 


from flask import Flask, redirect, url_for

# importacion de Rutas de vitsa
from opticall.application.routes.app.auth import auth_bp
from opticall.application.routes.app.forecasting import forecasting_bp
from opticall.application.routes.app.home import home_bp
from opticall.application.routes.app.monitoring import monitoring_bp
from opticall.application.routes.app.reports import reports_bp
from opticall.application.routes.app.scheduling import scheduling_bp
from opticall.application.routes.app.self_service import self_service_bp
from opticall.application.routes.app.shifts import shifts_bp
from opticall.application.routes.app.shared import shared_bp

# importacion de Rutas de  datos
# from opticall.application.routes.api.auth.autenticacion.login_route import auth_api

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

 

    # Registro de rutas de vista
    app.register_blueprint(home_bp, url_prefix="/app/")
    app.register_blueprint(auth_bp, url_prefix="/app/auth")
    app.register_blueprint(forecasting_bp, url_prefix="/app/forecast")
    app.register_blueprint(monitoring_bp, url_prefix="/app/monitoring")
    app.register_blueprint(reports_bp, url_prefix="/app/reports")
    app.register_blueprint(scheduling_bp, url_prefix="/app/scheduling")
    app.register_blueprint(self_service_bp, url_prefix="/app/self-service")
    app.register_blueprint(shifts_bp, url_prefix="/app/shifts")
    app.register_blueprint(shared_bp, url_prefix="/app/shared")

    # Registro de rutas de datos
    # app.register_blueprint(auth_api, url_prefix="/api/auth")

    @app.route('/')
    def index():
        return redirect(url_for('home.index'))
    
    @app.route('/about')
    def about():
        return "About Page"

    @app.route('/contact')
    def contact():
        return "Contact Page"
    
    @app.route('/help')
    def help():
        return "Help Page"
    
    return app
