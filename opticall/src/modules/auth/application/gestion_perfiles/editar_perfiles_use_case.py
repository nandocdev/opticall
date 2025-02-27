#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  gestion_perfiles
# @file        editar_perfiles_use_case
# @Date        2025-02-26 12:53:12
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from opticall.src.modules.auth.domain.entities import Profile
from opticall.src.modules.auth.domain.repositories import ProfileRepository
from opticall.src.modules.auth.application.exceptions import NombreDePerfilYaExisteError
# Importa la instancia de la base de datos
from opticall.src.shared.services.database import db

class EditarPerfilUseCase:
    """EditarPerfilUseCase Servicio para la edición de perfiles

    Args:
        profile_repository (ProfileRepository): Repositorio de perfiles

    Returns:
        Profile: Perfil editado
    """
    def __init__(self, profile_repository: ProfileRepository):
        self.profile_repository = profile_repository

    def execute(self, profile: Profile) -> Profile:
        if self.profile_repository.exists_by_name(profile.name):
            raise NombreDePerfilYaExisteError()
        try:
            self.profile_repository.update(profile)
            db.session.commit() 
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
        return profile