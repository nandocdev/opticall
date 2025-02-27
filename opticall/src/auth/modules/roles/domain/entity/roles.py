#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/roles/entity
# @subpackage  domain
# @file        roles
# @Date        2025-02-27 10:42:03
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from opticall.src.shared.services.database import Base
import datetime


class Roles(Base):
    __tablename__ = 'acc_roles'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(128), unique=True, nullable=False)
    descripcion = Column(String(100), nullable=False)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relacion con la tabla AccPermisos
    permisos = relationship("Permisos", back_populates="rol")

    def __repr__(self):
        return f"<Rol(nombre='{self.nombre}', estado='{self.estado}')>"
