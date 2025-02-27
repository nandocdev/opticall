#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/roles
# @subpackage  application
# @file        exists_role_use_case
# @Date        2025-02-27 15:40:46
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 


from opticall.src.auth.modules.roles.domain.repositories.roles_interface import RolesInterface


class ExistsRoleUseCase:
    def __init__(self, repository: RolesInterface):
        self.repository = repository

    def execute(self, id: int) -> bool:
        """Verifica si un rol existe por ID."""
        role = self.repository.get_by_id(id)
        return role is not None
