#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/domain
# @subpackage  repositories
# @file        role_repository
# @Date        2025-02-25 23:20:39
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 


from abc import ABC, abstractmethod
from typing import List, Optional
from opticall.src.modules.auth.domain.entities.role import Roles

class RoleRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Roles]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Roles]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Roles]:
        pass

    @abstractmethod
    def create_role(self, role: Roles) -> Roles:
        pass

    @abstractmethod
    def update_role(self, role: Roles) -> None:
        pass

    @abstractmethod
    def delete_role(self, role: Roles) -> None:
        pass
