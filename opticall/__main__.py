#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     Web/OptiCall
# @subpackage  opticall
# @file        __main__
# @Date        2025-02-25 11:45:54
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.application import create_app
import os

app = create_app()
app_name = os.environ.get('APP_NAME', 'OptiCall WFM')
footer_text = os.environ.get('FOOTER_TEXT', 'Copyright 2024')



@app.context_processor
def inject_config():
    return dict(app_name=app_name, footer_text=footer_text)


if __name__ == "__main__":
    app.run(debug=True)