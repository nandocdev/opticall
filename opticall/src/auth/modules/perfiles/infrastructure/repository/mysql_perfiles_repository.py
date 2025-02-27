#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     perfiles/infrastructure
# @subpackage  repository
# @file        mysql_perfiles_repository
# @Date        2025-02-27 11:17:19
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.auth.modules.perfiles.domain.interfaces.perfiles_interface import PerfilesInterface
from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles
from opticall.src.shared.services.database import SessionLocal
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)


class MysqlPerfilesRepository(PerfilesInterface):

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Perfiles]:
        """Retorna todos los perfiles en la base de datos.

        Returns:
            List[Perfiles]: Lista de perfiles existentes en la base de datos.
        """
        try:
            return self.session.query(Perfiles).all()
        except SQLAlchemyError as e:
            logger.error(
                f"Error al obtener todos los perfiles: {e}", exc_info=True)
            raise  # Re-lanzar la excepción para que la capa superior la maneje
    
    def get_by_id(self, id: int) -> Optional[Perfiles]:
        """Retorna un perfil en la base de datos por ID.

        Args:
            id (int): ID del perfil a obtener.

        Returns:
            Optional[Perfiles]: Perfil encontrado o None si no existe.
        """
        try:
            return self.session.query(Perfiles).filter(Perfiles.id == id).first()
        except SQLAlchemyError as e:
            logger.error(
                f"Error al obtener el perfil con ID {id}: {e}", exc_info=True)
            raise

    def get_by_name(self, name: str) -> Optional[Perfiles]:
        """Retorna un perfil en la base de datos por nombre.

        Args:
            name (str): Nombre del perfil a obtener.

        Returns:
            Optional[Perfiles]: Perfil encontrado o None si no existe.
        """
        try:
            return self.session.query(Perfiles).filter(Perfiles.nombre == name).first()
        except SQLAlchemyError as e:
            logger.error(
                f"Error al obtener el perfil con nombre {name}: {e}", exc_info=True)
            raise
    
    def get_by_status(self, status: bool) -> List[Perfiles]:
        """Retorna una lista de perfiles en la base de datos por estado.

        Args:
            status (bool): Estado del perfil a obtener.

        Returns:
            List[Perfiles]: Lista de perfiles encontrados con el estado especificado.
        """
        try:
            perfiles = self.session.query(Perfiles).filter(Perfiles.estado == status).all()
            return perfiles
        except SQLAlchemyError as e:
            logger.error(
                f"Error al obtener perfiles con estado {status}: {e}", exc_info=True)
            raise
    
    def create_profile(self, profile: Perfiles) -> Perfiles:
        """Crea un perfil en la base de datos.

        Args:
            profile (Perfiles): Perfil a crear.

        Returns:
            Perfiles: Perfil creado en la base de datos.
        """
        try:
            self.session.add(profile)
            self.session.commit()
            # Refrescar para obtener el ID generado
            self.session.refresh(profile)
            return profile
        except SQLAlchemyError as e:
            logger.error(f"Error al crear el perfil: {e}", exc_info=True)
            self.session.rollback()
            raise


    def update_profile(self, profile: Perfiles) -> None:
        """Modifica un perfil en la base de datos.

        Args:
            profile (Perfiles): Perfil a actualizar.
        """
        try:
            # En lugar de buscar y actualizar, actualizamos directamente
            result = self.session.query(Perfiles).filter(Perfiles.id == profile.id).update({
                Perfiles.nombre: profile.nombre,
                Perfiles.descripcion: profile.descripcion,
                Perfiles.estado: profile.estado
            })
            if result == 0:
                raise ValueError(
                    f"No se encontró el perfil con ID {profile.id} para actualizar.")

            self.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"Error al actualizar el perfil: {e}", exc_info=True)
            self.session.rollback()
            raise
    
    def delete_profile(self, profile: Perfiles) -> None:
        """Elimina un perfil en la base de datos.

        Args:
            profile (Perfiles): Perfil a eliminar.
        """
        try:
            # Borrar directamente usando el ID
            result = self.session.query(Perfiles).filter(
                Perfiles.id == profile.id).delete()
            if result == 0:
                raise ValueError(
                    f"No se encontró el perfil con ID {profile.id} para eliminar.")
            self.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"Error al eliminar el perfil: {e}", exc_info=True)
            self.session.rollback()
            raise

    def exists_by_name(self, name: str) -> bool:
        """Verifica si un perfil existe en la base de datos por nombre.

        Args:
            name (str): Nombre del perfil a verificar.

        Returns:
            bool: Verdadero si el perfil existe, de lo contrario falso.
        """
        try:
            return self.session.query(Perfiles).filter(Perfiles.nombre == name).count() > 0
        except SQLAlchemyError as e:
            logger.error(
                f"Error al verificar si existe el perfil con nombre {name}: {e}", exc_info=True)
            raise
    
    def exists_by_id(self, id: int) -> bool:
        """Verifica si un perfil existe en la base de datos por ID.
        
        Args:
            id (int): ID del perfil a verificar.
        
        Returns:
            bool: Verdadero si el perfil existe, de lo contrario falso.
        """
        try:
            return self.session.query(Perfiles).filter(Perfiles.id == id).count() > 0
        except SQLAlchemyError as e:
            logger.error(
                f"Error al verificar si existe el perfil con ID {id}: {e}", exc_info=True)
            raise
