#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     OptiCall/opticall
# @subpackage  application
# @file        __init__
# @Date        2025-02-25 12:04:16
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 


from flask import Flask
from opticall.application.routes.auth import auth_bp
from opticall.application.routes.forecasting import forecasting_bp
from opticall.application.routes.home import home_bp
from opticall.application.routes.monitoring import monitoring_bp
from opticall.application.routes.reports import reports_bp
from opticall.application.routes.scheduling import scheduling_bp
from opticall.application.routes.self_service import self_service_bp
from opticall.application.routes.shifts import shifts_bp
from opticall.application.routes.shared import shared_bp


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Registrar Blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(forecasting_bp, url_prefix="/forecast")
    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(monitoring_bp, url_prefix="/monitoring")
    app.register_blueprint(reports_bp, url_prefix="/reports")
    app.register_blueprint(scheduling_bp, url_prefix="/scheduling")
    app.register_blueprint(self_service_bp, url_prefix="/self-service")
    app.register_blueprint(shifts_bp, url_prefix="/shifts")
    app.register_blueprint(shared_bp, url_prefix="/shared")

    return app
