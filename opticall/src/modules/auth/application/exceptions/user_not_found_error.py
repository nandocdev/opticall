#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  exceptions
# @file        user_not_found_error
# @Date        2025-02-26 10:59:20
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

class UserNotFoundError(Exception):
    def __init__(self, message: str = "Usuario no encontrado"):
        super().__init__(f"Usuario no encontrado: {message}")
