#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     perfiles/domain
# @subpackage  repositories
# @file        perfiles_interface
# @Date        2025-02-27 11:11:45
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from abc import ABC, abstractmethod
from typing import List, Optional
from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles

class PerfilesInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[Perfiles]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Perfiles]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Perfiles]:
        pass

    def get_by_status(self, status: bool) -> List[Perfiles]:
        pass

    @abstractmethod
    def create_profile(self, profile: Perfiles) -> Perfiles:
        pass

    @abstractmethod
    def update_profile(self, profile: Perfiles) -> None:
        pass

    @abstractmethod
    def delete_profile(self, profile: Perfiles) -> None:
        pass

    @abstractmethod
    def exists_by_name(self, name: str) -> bool:
        pass

    @abstractmethod
    def exists_by_id(self, id: int) -> bool:
        pass
