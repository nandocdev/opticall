#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/domain
# @subpackage  repositories
# @file        user_repository
# @Date        2025-02-25 23:06:39
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description define una interfaz para el repositorio de usuarios con metodos crud

from abc import ABC, abstractmethod
from typing import List, Optional
from opticall.src.modules.auth.domain.entities.user import Usuarios

class UserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Usuarios]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Usuarios]:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[Usuarios]:
        pass

    @abstractmethod
    def create_user(self, user: Usuarios) -> Usuarios:
        pass

    @abstractmethod
    def update_user(self, user: Usuarios) -> None:
        pass

    @abstractmethod
    def delete_user(self, user: Usuarios) -> None:
        pass

