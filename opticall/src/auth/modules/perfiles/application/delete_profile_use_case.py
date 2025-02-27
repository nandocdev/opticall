#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/perfiles
# @subpackage  application
# @file        delete_profile_use_case
# @Date        2025-02-27 13:07:32
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.perfiles.domain.interfaces.perfiles_interface import PerfilesInterface


class DeleteProfileUseCase:
    def __init__(self, repository: PerfilesInterface):
        self.repository = repository

    def execute(self, id: int) -> None:
        profile = self.repository.get_by_id(id)
        if profile is None:
            raise ValueError(f"No existe un perfil con el ID '{id}'")
        self.repository.delete_profile(profile)
