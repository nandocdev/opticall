#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/infrastructure
# @subpackage  repositories
# @file        sqlalchemy_permission_repository
# @Date        2025-02-26 08:20:37
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description


from opticall.src.modules.auth.domain.entities.permission import Permisos
from opticall.src.modules.auth.domain.repositories.permission_repository import PermissionRepository
from typing import List, Optional

class SqlAlchemyPermissionRepository(PermissionRepository):
    def __init__(self, session):
        self.session = session

    # 
    def create(self, permission: Permisos):
        self.session.add(permission)
        self.session.commit()

    def get_by_name(self, name: str) -> Permisos:
        return self.session.query(Permisos).filter(Permisos.name == name).first()

    def get_by_id(self, id: int) -> Permisos:
        return self.session.query(Permisos).filter(Permisos.id == id).first()

    def get_all(self) -> List[Permisos]:
        return self.session.query(Permisos).all()
    
    def get_by_profile(self, id_profile: int):
        return self.session.query(Permisos).filter(Permisos.profile_id == id_profile).all()
    
    def get_by_role(self, id_role: int):
        return self.session.query(Permisos).filter(Permisos.role_id == id_role).all()

    def update(self, permission: Permisos):
        self.session.add(permission)
        self.session.commit()

    def delete(self, permission: Permisos):
        if permission is not None:
            self.session.delete(permission)
            self.session.commit()
        else:
            raise ValueError("Cannot delete a None permission.")
