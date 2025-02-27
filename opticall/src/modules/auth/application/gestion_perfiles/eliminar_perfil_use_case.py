#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  gestion_perfiles
# @file        eliminar_perfil_use_case
# @Date        2025-02-26 13:01:47
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Eliminación logica de un perfil, cambiando el estado a inactivo

from opticall.src.modules.auth.domain.entities import Profile
from opticall.src.modules.auth.domain.repositories import ProfileRepository
from opticall.src.modules.auth.application.exceptions import PerfilNoExisteError
# Importa la instancia de la base de datos
from opticall.src.shared.services.database import db

class EliminarPerfilUseCase:
    """EliminarPerfilUseCase Servicio para la eliminación de perfiles

    Args:
        profile_repository (ProfileRepository): Repositorio de perfiles

    Returns:
        Profile: Perfil eliminado
    """
    def __init__(self, profile_repository: ProfileRepository):
        self.profile_repository = profile_repository

    def execute(self, profile: Profile) -> Profile:
        if not self.profile_repository.exists_by_id(profile.id):
            raise PerfilNoExisteError()
        try:
            profile.active = False
            self.profile_repository.update(profile)
            db.session.commit() 
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
        return profile