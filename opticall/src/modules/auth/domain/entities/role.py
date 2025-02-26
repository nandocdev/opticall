#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/domain
# @subpackage  entities
# @file        role
# @Date        2025-02-25 23:02:19
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 
"""
CREATE TABLE `acc_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(128) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""

import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from opticall.src.shared.services.database import Base

class Roles(Base):
    __tablename__ = 'acc_roles'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    descripcion = Column(String)
    estado = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
