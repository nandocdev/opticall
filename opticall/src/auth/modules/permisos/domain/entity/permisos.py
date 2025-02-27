#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/permisos
# @subpackage  domain
# @file        permisos
# @Date        2025-02-27 10:41:44
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from opticall.src.shared.services.database import Base
import datetime


class Permisos(Base):
    __tablename__ = 'acc_permisos'

    id = Column(Integer, primary_key=True, index=True)
    id_perfil = Column(Integer, ForeignKey('acc_perfiles.id'))
    id_rol = Column(Integer, ForeignKey('acc_roles.id'))
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    perfil = relationship("Perfil", back_populates="permisos")
    rol = relationship("Roles", back_populates="permisos")

    def __repr__(self):
        return f"<Permisos(id_perfil={self.id_perfil}, id_rol={self.id_rol}, estado={self.estado})>"
