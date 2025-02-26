#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/infrastructure
# @subpackage  repositories
# @file        sqlalchemy_profile_repository
# @Date        2025-02-26 07:50:11
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.modules.auth.domain.entities.profile import Perfiles
from opticall.src.modules.auth.domain.repositories.profile_repository import ProfileRepository

class SqlAlchemyProfileRepository(ProfileRepository):
    def __init__(self, session):
        self.session = session

    def create(self, profile: Perfiles):
        self.session.add(profile)
        self.session.commit()

    def get_by_name(self, name: str) -> Perfiles:
        return self.session.query(Perfiles).filter(Perfiles.name == name).first()

    def get_by_id(self, id: int) -> Perfiles:
        return self.session.query(Perfiles).filter(Perfiles.id == id).first()

    def get_all(self):
        return self.session.query(Perfiles).all()

    def update(self, profile: Perfiles):
        self.session.add(profile)
        self.session.commit()

    def delete(self, profile: Perfiles):
        self.session.delete(profile)
        self.session.commit()
