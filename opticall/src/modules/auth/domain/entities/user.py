#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/domain
# @subpackage  entities
# @file        user
# @Date        2025-02-25 22:54:22
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Entidad de dominio de usuario
"""
CREATE TABLE `acc_usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_funcionario` int(11) NOT NULL,
  `usuario` varchar(64) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id_perfil` int(11) NOT NULL,
  `activo` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`),
  KEY `id_perfil` (`id_perfil`),
  KEY `idx_usuarios_email` (`usuario`),
  KEY `acc_usuarios_emp_funcionarios_FK` (`id_funcionario`),
  CONSTRAINT `acc_usuarios_emp_funcionarios_FK` FOREIGN KEY (`id_funcionario`) REFERENCES `emp_funcionarios` (`id`),
  CONSTRAINT `acc_usuarios_ibfk_1` FOREIGN KEY (`id_perfil`) REFERENCES `acc_perfiles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from opticall.src.shared.services.database import Base
from opticall.src.modules.auth.domain.value_objects.password_value_object import PasswordValueObject


class Usuarios(Base):
    __tablename__ = 'acc_usuarios'

    id = Column(Integer, primary_key=True, index=True)
    id_funcionario = Column(Integer, ForeignKey('emp_funcionarios.id'))
    usuario = Column(String, unique=True, index=True)
    password = Column(PasswordValueObject)
    id_perfil = Column(Integer, ForeignKey('acc_perfiles.id'))
    activo = Column(Integer, default=1)

    funcionario = relationship('Funcionario', back_populates='usuario')
    perfil = relationship('Perfil', back_populates='usuario')

    def __repr__(self):
        return f"<Usuario(usuario='{self.usuario}', activo='{self.activo}')>"


