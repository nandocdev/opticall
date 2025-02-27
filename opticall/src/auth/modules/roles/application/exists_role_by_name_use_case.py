#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/roles
# @subpackage  application
# @file        exists_role_by_name_use_case
# @Date        2025-02-27 15:41:18
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.roles.domain.repositories.roles_interface import RolesInterface


class ExistsRoleByNameUseCase:
    def __init__(self, repository: RolesInterface):
        self.repository = repository

    def execute(self, name: str) -> bool:
        """Verifica si un rol existe por Nombre."""
        roles = self.repository.get_all()
        for role in roles:
            if role.nombre == name:
                return True
        return False
