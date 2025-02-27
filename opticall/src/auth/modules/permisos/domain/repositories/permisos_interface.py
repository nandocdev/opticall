#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     permisos/domain
# @subpackage  repositories
# @file        permisos_interface
# @Date        2025-02-27 16:23:33
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from abc import ABC, abstractmethod
from typing import List
from opticall.src.auth.modules.permisos.domain.entity.permisos import Permiso

class PermisosInterface:
    @abstractmethod
    def get_all(self) -> List[Permiso]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Permiso:
        pass

    @abstractmethod
    def get_by_perfil(self, id_perfil: int) -> Permiso:
        pass

    @abstractmethod
    def get_by_rol(self, id_rol: int) -> Permiso:
        pass

    @abstractmethod
    def create(self, permiso: Permiso) -> Permiso:
        pass

    @abstractmethod
    def update(self, permiso: Permiso) -> Permiso:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
