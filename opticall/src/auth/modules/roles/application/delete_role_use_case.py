#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/roles
# @subpackage  application
# @file        delete_role_use_case
# @Date        2025-02-27 15:39:36
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.roles.domain.entity.roles import Roles
from opticall.src.auth.modules.roles.domain.repositories.roles_interface import RolesInterface


class DeleteRoleUseCase:
    def __init__(self, repository: RolesInterface):
        self.repository = repository

    def execute(self, id: int) -> None:
        """Elimina un rol."""
        role = self.repository.get_by_id(id)
        if role is None:
            raise ValueError(f"No se encontró un rol con el ID '{id}'.")
        self.repository.delete(role)
