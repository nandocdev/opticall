#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  gestion_perfiles
# @file        crear_perfiles_use_case
# @Date        2025-02-26 12:24:55
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

# src/modules/auth/application/gestion_perfiles/crear_perfil_use_case.py
from opticall.src.modules.auth.domain.entities import Profile
from opticall.src.modules.auth.domain.repositories import ProfileRepository
from opticall.src.modules.auth.application.exceptions import NombreDePerfilYaExisteError
# Importa la instancia de la base de datos
from opticall.src.shared.services.database import db

class CrearPerfilUseCase:
    """CrearPerfilUseCase Servicio para la creación de perfiles

    Args:
        profile_repository (ProfileRepository): Repositorio de perfiles

    Returns:
        Profile: Perfil creado
    """
    def __init__(self, profile_repository: ProfileRepository):
        self.profile_repository = profile_repository

    def execute(self, profile: Profile) -> Profile:
        if self.profile_repository.exists_by_name(profile.name):
            raise NombreDePerfilYaExisteError()
        try:
            self.profile_repository.create(profile)
            db.session.commit() 
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
        return profile

# src/modules/auth/application/gestion_perfiles/crear_perfiles_use_case.py