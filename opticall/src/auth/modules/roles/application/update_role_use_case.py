#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/roles
# @subpackage  application
# @file        update_role_use_case
# @Date        2025-02-27 15:38:47
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.roles.domain.entity.roles import Roles
from opticall.src.auth.modules.roles.domain.repositories.roles_interface import RolesInterface
from typing import Optional

class UpdateRoleUseCase:
    def __init__(self, repository: RolesInterface):
        self.repository = repository

    def execute(self, id: int, nombre: str = None, descripcion: str = None, estado: bool = None) -> Roles:
        """Actualiza un rol existente."""
        role = self.repository.get_by_id(id)
        if role is None:
            raise ValueError(f"No se encontró un rol con el ID '{id}'.")

        # Actualiza los atributos si se proporcionan
        if nombre is not None:
            role.nombre = nombre
        if descripcion is not None:
            role.descripcion = descripcion
        if estado is not None:
            role.estado = estado

        # Usamos el método save para actualizar
        return self.repository.save(role)
