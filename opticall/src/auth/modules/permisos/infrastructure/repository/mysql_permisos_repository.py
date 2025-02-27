#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     permisos/infrastructure
# @subpackage  repository
# @file        mysql_permisos_repository
# @Date        2025-02-27 16:26:11
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from calendar import c
from typing import List
from opticall.src.auth.modules.permisos.domain.entity.permisos import Permiso
from opticall.src.auth.modules.permisos.domain.repositories.permisos_interface import PermisosInterface
from opticall.src.shared.services.database import SessionLocal
from sqlalchemy.orm import Session

class MysqlPermisosRepository(PermisosInterface):
    def get_all(self) -> List[Permiso]:
        with SessionLocal() as session:
            return session.query(Permiso).all()

    def get_by_id(self, id: int) -> Permiso:
        with SessionLocal() as session:
            return session.query(Permiso).filter(Permiso.id == id).first()

    def get_by_perfil(self, id_perfil: int) -> Permiso:
        with SessionLocal() as session:
            return session.query(Permiso).filter(Permiso.id_perfil == id_perfil).first()

    def get_by_rol(self, id_rol: int) -> Permiso:
        with SessionLocal() as session:
            return session.query(Permiso).filter(Permiso.id_rol == id_rol).first()

    def create(self, permiso: Permiso) -> Permiso:
        with SessionLocal() as session:
            session.add(permiso)
            session.commit()
            session.refresh(permiso)
            return permiso

    def update(self, permiso: Permiso) -> Permiso:
        with SessionLocal() as session:
            session.query(Permiso).filter(Permiso.id == permiso.id).update(permiso)
            session.commit()
            session.refresh(permiso)
            return permiso

    def delete(self, id: int) -> None:
        with SessionLocal() as session:
            session.query(Permiso).filter(Permiso.id == id).delete()
            session.commit()
