#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  exceptions
# @file        credentials_invalid_error
# @Date        2025-02-26 10:58:42
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

class CredentialsInvalidError(Exception):
    def __init__(self, message: str = "Credenciales invalidas"):
        super().__init__(f"Credenciales invalidas: {message}")
