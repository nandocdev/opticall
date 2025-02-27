#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/perfiles
# @subpackage  application
# @file        list_profiles_use_case
# @Date        2025-02-27 12:58:06
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles
from opticall.src.auth.modules.perfiles.domain.interfaces.perfiles_interface import PerfilesInterface
from typing import List

class ListProfilesUseCase:
    def __init__(self, repository: PerfilesInterface):
        self.repository = repository

    def execute(self) -> List[Perfiles]:
        return self.repository.get_all()
