#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/infrastructure
# @subpackage  repositories
# @file        sqlalchemy_profile_repository
# @Date        2025-02-26 07:50:11
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.modules.auth.domain.entities.profile import Perfiles
from opticall.src.modules.auth.domain.repositories.profile_repository import ProfileRepository
from typing import List, Optional
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)


class SqlAlchemyProfileRepository(ProfileRepository):
    def __init__(self, session: Session):
        
        self.session = session

    def get_all(self) -> List[Perfiles]:
        try:
            return self.session.query(Perfiles).all()
        except Exception as e:
            logger.error(
                f"Error al obtener todos los perfiles: {e}", exc_info=True)
            raise

    def get_by_id(self, id: int) -> Optional[Perfiles]:
        try:
            return self.session.query(Perfiles).filter(Perfiles.id == id).first()
        except Exception as e:
            logger.error(
                f"Error al obtener el perfil con ID {id}: {e}", exc_info=True)
            raise

    def get_by_name(self, name: str) -> Optional[Perfiles]:
        try:
            return self.session.query(Perfiles).filter(Perfiles.name == name).first()
        except Exception as e:
            logger.error(
                f"Error al obtener el perfil con nombre {name}: {e}", exc_info=True)
            raise

    def get_by_status(self, status: bool) -> List[Perfiles]:
        try:
            perfiles = self.session.query(Perfiles).filter(Perfiles.estado == status).all()
            return perfiles
        except Exception as e:
            logger.error(
                f"Error al obtener perfiles con estado {status}: {e}", exc_info=True)
            raise

    # Retorna None porque no devuelve nada significativo
    def create_profile(self, profile: Perfiles) -> None:
        try:
            self.session.add(profile)
            self.session.commit()  # Commit la sesion dentro del metodo.
            self.session.refresh(profile)  # Refresca el perfil
        except Exception as e:
            logger.error(f"Error al crear el perfil: {e}", exc_info=True)
            self.session.rollback()  # Rollback en caso de error.
            raise

    # Retorna None porque no devuelve nada significativo
    def update_profile(self, profile: Perfiles) -> None:
        try:
            self.session.add(profile)  # usar merge
            self.session.commit()
            self.session.refresh(profile)  # Refresca el perfil
        except Exception as e:
            logger.error(f"Error al actualizar el perfil: {e}", exc_info=True)
            self.session.rollback()  # Rollback en caso de error.
            raise

    # Retorna None porque no devuelve nada significativo
    def delete_profile(self, profile: Perfiles) -> None:
        try:
            self.session.delete(profile)
            self.session.commit()
        except Exception as e:
            logger.error(f"Error al eliminar el perfil: {e}", exc_info=True)
            self.session.rollback()  # Rollback en caso de error.
            raise

    def exists_by_name(self, name: str) -> bool:
        try:
            return self.session.query(Perfiles).filter(Perfiles.name == name).count() > 0
        except Exception as e:
            logger.error(
                f"Error al verificar la existencia del perfil por nombre {name}: {e}", exc_info=True)
            raise

    def exists_by_id(self, id: int) -> bool:
        try:
            return self.session.query(Perfiles).filter(Perfiles.id == id).count() > 0
        except Exception as e:
            logger.error(
                f"Error al verificar la existencia del perfil por ID {id}: {e}", exc_info=True)
            raise
