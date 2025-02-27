#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/roles
# @subpackage  application
# @file        change_role_status_use_case
# @Date        2025-02-27 15:40:12
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.roles.domain.entity.roles import Roles
from opticall.src.auth.modules.roles.domain.repositories.roles_interface import RolesInterface


class ChangeRoleStatusUseCase:
    def __init__(self, repository: RolesInterface):
        self.repository = repository

    def execute(self, id: int, estado: bool) -> Roles:
        """Cambia el estado (activo/inactivo) de un rol."""
        role = self.repository.get_by_id(id)
        if role is None:
            raise ValueError(f"No se encontró un rol con el ID '{id}'.")
        role.estado = estado
        return self.repository.save(role)
