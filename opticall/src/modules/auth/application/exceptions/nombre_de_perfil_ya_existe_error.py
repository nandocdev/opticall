#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  exceptions
# @file        nombre_de_perfil_ya_existe_error
# @Date        2025-02-26 12:49:57
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

class NombreDePerfilYaExisteError(Exception):
    def __init__(self, message: str = "El nombre de perfil ya existe"):
        super().__init__(f"El nombre de perfil ya existe: {message}")
