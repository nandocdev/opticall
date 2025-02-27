#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     roles/domain
# @subpackage  repositories
# @file        roles_interface
# @Date        2025-02-27 15:23:48
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from abc import ABC, abstractmethod
from typing import List 
from opticall.src.auth.modules.roles.domain.entity.roles import Roles

class RolesInterface(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Roles:
        pass

    @abstractmethod
    def get_all(self) -> List[Roles]:
        pass

    @abstractmethod
    def save(self, roles: Roles) -> Roles:
        pass

    @abstractmethod
    def delete(self, roles: Roles) -> None:
        pass
