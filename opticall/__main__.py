#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     Web/OptiCall
# @subpackage  opticall
# @file        __main__
# @Date        2025-02-25 11:45:54
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)