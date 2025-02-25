#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        __init__
# @Date        2025-02-25 11:14:19
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description registration of all blueprints

from .home import home
from .auth import auth
from .forecasting import forecasting
from .monitoring import monitoring
from .reports import reports
from .scheduling import schedule
from .self_service import self_service
from .shifts import shifts

def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(forecasting, url_prefix='/forecasting')
    app.register_blueprint(monitoring, url_prefix='/monitoring')
    app.register_blueprint(reports, url_prefix='/reports')
    app.register_blueprint(schedule, url_prefix='/schedule')
    app.register_blueprint(self_service, url_prefix='/self_service')
    app.register_blueprint(shifts, url_prefix='/shifts')




