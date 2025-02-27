#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/domain
# @subpackage  repositories
# @file        profile_repository
# @Date        2025-02-25 23:20:05
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from abc import ABC, abstractmethod
from typing import List, Optional
from opticall.src.modules.auth.domain.entities.profile import Perfiles

class ProfileRepository(ABC):
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
