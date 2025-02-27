#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/roles
# @subpackage  application
# @file        list_roles_use_case
# @Date        2025-02-27 15:38:31
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.roles.domain.entity.roles import Roles
from opticall.src.auth.modules.roles.domain.repositories.roles_interface import RolesInterface
from typing import List


class ListRolesUseCase:
    def __init__(self, repository: RolesInterface):
        self.repository = repository

    def execute(self) -> List[Roles]:
        """Lista todos los roles."""
        return self.repository.get_all()
