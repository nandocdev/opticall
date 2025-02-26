#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/infrastructure
# @subpackage  repositories
# @file        sqlalchemy_role_repository
# @Date        2025-02-26 08:20:14
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.modules.auth.domain.entities.role import Roles
from opticall.src.modules.auth.domain.repositories.role_repository import RoleRepository

class SqlAlchemyRoleRepository(RoleRepository):
    def __init__(self, session):
        self.session = session

    def create(self, role: Roles):
        self.session.add(role)
        self.session.commit()

    def get_by_name(self, name: str) -> Roles:
        return self.session.query(Roles).filter(Roles.name == name).first()

    def get_by_id(self, id: int) -> Roles:
        return self.session.query(Roles).filter(Roles.id == id).first()

    def get_all(self):
        return self.session.query(Roles).all()

    def update(self, role: Roles):
        self.session.add(role)
        self.session.commit()

    def delete(self, role: Roles):
        self.session.delete(role)
        self.session.commit()
