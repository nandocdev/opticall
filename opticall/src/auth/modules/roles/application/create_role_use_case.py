#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/roles
# @subpackage  application
# @file        create_role_use_case
# @Date        2025-02-27 15:37:19
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.roles.domain.entity.roles import Roles
from opticall.src.auth.modules.roles.domain.repositories.roles_interface import RolesInterface


class CreateRoleUseCase:
    def __init__(self, repository: RolesInterface):
        self.repository = repository

    def execute(self, nombre: str, descripcion: str, estado: bool) -> Roles:
        """Crea un nuevo rol."""

        # TODO: implementar la validacion de los datos

        role = Roles(nombre=nombre, descripcion=descripcion, estado=estado)
        return self.repository.save(role)
