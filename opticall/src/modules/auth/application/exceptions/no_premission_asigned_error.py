#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  exceptions
# @file        no_premission_asigned_error
# @Date        2025-02-26 11:26:34
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

class NoPremissionAsignedError(Exception):
    def __init__(self, message: str = "No se han asignado permisos al usuario"):
        super().__init__(f"No se han asignado permisos al usuario: {message}")
