#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/perfiles
# @subpackage  application
# @file        update_profile_use_case
# @Date        2025-02-27 13:06:52
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 


from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles
from opticall.src.auth.modules.perfiles.domain.interfaces.perfiles_interface import PerfilesInterface


class UpdateProfileUseCase:
    def __init__(self, repository: PerfilesInterface):
        self.repository = repository

    def execute(self, id: int, nombre: str = None, descripcion: str = None, estado: bool = None) -> None:
        profile = self.repository.get_by_id(id)
        if profile is None:
            raise ValueError(f"No existe un perfil con el ID '{id}'")

        if nombre and nombre != profile.nombre:
            if self.repository.exists_by_name(nombre):
                raise ValueError(
                    f"Ya existe un perfil con el nombre '{nombre}'")
            profile.nombre = nombre
        if descripcion:
            profile.descripcion = descripcion
        if estado is not None:
            profile.estado = estado

        self.repository.update_profile(profile)
