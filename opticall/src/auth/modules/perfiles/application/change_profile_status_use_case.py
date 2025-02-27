#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/perfiles
# @subpackage  application
# @file        change_profile_status_use_case
# @Date        2025-02-27 13:07:59
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles
from opticall.src.auth.modules.perfiles.domain.interfaces.perfiles_interface import PerfilesInterface


class ChangeProfileStatusUseCase:
    def __init__(self, repository: PerfilesInterface):
        self.repository = repository

    def execute(self, id: int, estado: bool) -> None:
        profile = self.repository.get_by_id(id)
        if profile is None:
            raise ValueError(f"No existe un perfil con el ID '{id}'")
        profile.estado = estado
        self.repository.update_profile(profile)
