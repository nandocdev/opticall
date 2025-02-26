#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/domain
# @subpackage  repositories
# @file        permission_repository
# @Date        2025-02-25 23:21:01
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from abc import ABC, abstractmethod
from typing import List, Optional
from opticall.src.modules.auth.domain.entities.permission import Permisos

class PermissionRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Permisos]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Permisos]:
        pass

    @abstractmethod
    def get_by_profile(self, id_profile: int) -> Optional[Permisos]:
        pass

    @abstractmethod
    def get_by_role(self, id_role: int) -> Optional[Permisos]:
        pass

    @abstractmethod
    def create_permission(self, permission: Permisos) -> Permisos:
        pass

    @abstractmethod
    def update_permission(self, permission: Permisos) -> None:
        pass

    @abstractmethod
    def delete_permission(self, permission: Permisos) -> None:
        pass
