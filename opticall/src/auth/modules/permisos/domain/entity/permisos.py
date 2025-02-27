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


class Permiso(Base):
    __tablename__ = "acc_permisos"

    id = Column(Integer, primary_key=True, index=True)
    id_perfil = Column(Integer, ForeignKey(
        "acc_perfiles.id", ondelete="CASCADE"), nullable=False)
    id_rol = Column(Integer, ForeignKey(
        "acc_roles.id", ondelete="CASCADE"), nullable=False)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    perfil = relationship("Perfil", back_populates="permisos")
    rol = relationship("Rol", back_populates="permisos")

    def __repr__(self):
        return f"<Permiso(perfil_id='{self.id_perfil}', rol_id='{self.id_rol}', estado='{self.estado}')>"
