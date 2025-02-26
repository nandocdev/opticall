#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/domain
# @subpackage  entities
# @file        permission
# @Date        2025-02-25 23:02:36
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 
"""
CREATE TABLE `acc_permisos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_perfil` int(11) NOT NULL,
  `id_rol` int(11) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `idx_permisos_perfil` (`id_perfil`),
  KEY `idx_permisos_rol` (`id_rol`),
  CONSTRAINT `acc_permisos_ibfk_1` FOREIGN KEY (`id_perfil`) REFERENCES `acc_perfiles` (`id`) ON DELETE CASCADE,
  CONSTRAINT `acc_permisos_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `acc_roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from opticall.src.shared.services.database import Base

class Permisos(Base):
    __tablename__ = 'acc_permisos'

    id = Column(Integer, primary_key=True, index=True)
    id_perfil = Column(Integer, ForeignKey('acc_perfiles.id'))
    id_rol = Column(Integer, ForeignKey('acc_roles.id'))
    estado = Column(Integer, default=1)

    perfil = relationship('Perfiles', back_populates='permiso')
    rol = relationship('Roles', back_populates='permiso')
