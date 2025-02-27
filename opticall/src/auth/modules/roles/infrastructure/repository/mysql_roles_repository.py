#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     roles/infrastructure
# @subpackage  repository
# @file        mysql_roles_repository
# @Date        2025-02-27 15:25:29
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.roles.domain.entity.roles import Roles
from opticall.src.auth.modules.roles.domain.repositories.roles_interface import RolesInterface
from opticall.src.shared.services.database import SessionLocal
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging


logger = logging.getLogger(__name__)

class MysqlRolesRepository(RolesInterface):
    
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Roles]:
        """Retorna todos los roles en la base de datos.

        Returns:
            List[Roles]: Lista de roles existentes en la base de datos.
        """
        try:
            return self.session.query(Roles).all()
        except SQLAlchemyError as e:
            logger.error(
                f"Error al obtener todos los roles: {e}", exc_info=True)
            raise  # Re-lanzar la excepción para que la capa superior la maneje
    
    def get_by_id(self, id: int) -> Optional[Roles]:
        """Retorna un rol en la base de datos por ID.

        Args:
            id (int): ID del rol a obtener.

        Returns:
            Optional[Roles]: Rol encontrado o None si no existe.
        """
        try:
            return self.session.query(Roles).filter(Roles.id == id).first()
        except SQLAlchemyError as e:
            logger.error(
                f"Error al obtener el rol con ID {id}: {e}", exc_info=True)
            raise

    def save(self, roles: Roles) -> Roles:
        """Guarda un rol en la base de datos.

        Args:
            roles (Roles): Rol a guardar.

        Returns:
            Roles: Rol guardado.
        """
        try:
            self.session.add(roles)
            self.session.commit()
            return roles
        except SQLAlchemyError as e:
            logger.error(
                f"Error al guardar el rol: {e}", exc_info=True)
            self.session.rollback()
            raise

    def delete(self, roles: Roles) -> None:
        """Elimina un rol de la base de datos.

        Args:
            roles (Roles): Rol a eliminar.
        """
        try:
            self.session.delete(roles)
            self.session.commit()
        except SQLAlchemyError as e:
            logger.error(
                f"Error al eliminar el rol: {e}", exc_info=True)
            self.session.rollback()
            raise