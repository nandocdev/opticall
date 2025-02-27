#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/perfiles
# @subpackage  domain
# @file        perfil
# @Date        2025-02-27 10:29:02
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from opticall.src.shared.services.database import Base
import datetime


class Perfiles(Base):
    __tablename__ = 'acc_perfiles'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(100), nullable=False)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relacion con la tabla AccUsuarios
    usuarios = relationship("Usuarios", back_populates="perfil")

    # Relacion con la tabla AccPermisos
    permisos = relationship("Permisos", back_populates="perfil")

    def __repr__(self):
        return f"<Perfil(nombre='{self.nombre}', estado='{self.estado}')>"
