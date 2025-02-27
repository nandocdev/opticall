#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     modules/usuarios
# @subpackage  domain
# @file        usuarios
# @Date        2025-02-27 10:49:27
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from opticall.src.shared.services.database import Base
import datetime


class Usuarios(Base):
    __tablename__ = 'acc_usuarios'

    id = Column(Integer, primary_key=True, index=True)
    id_funcionario = Column(Integer, ForeignKey('emp_funcionarios.id'))
    usuario = Column(String(64), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    id_perfil = Column(Integer, ForeignKey('acc_perfiles.id'))
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    funcionario = relationship("Funcionarios", back_populates="usuarios")
    perfil = relationship("Perfil", back_populates="usuarios")

    def __repr__(self):
        return f"<Usuarios(usuario='{self.usuario}', activo='{self.activo}')>"

    def check_password(self, password: str) -> bool:
        # implementacion con bcrypt
        # bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
        pass
