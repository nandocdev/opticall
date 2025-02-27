#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/perfiles
# @subpackage  application
# @file        create_profile_use_case
# @Date        2025-02-27 12:48:01
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles
from opticall.src.auth.modules.perfiles.domain.interfaces.perfiles_interface import PerfilesInterface

class CreateProfileUseCase:
    def __init__(self, repository: PerfilesInterface):
        self.repository = repository

    def execute(self, profile: Perfiles) -> Perfiles:
        if self.repository.exists_by_name(profile.nombre):
            raise ValueError(
                f"Ya existe un perfil con el nombre '{profile.nombre}'")
        profile.estado = True
        return self.repository.create_profile(profile)