#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  gestion_perfiles
# @file        listar_perfiles_by_estado
# @Date        2025-02-26 13:14:23
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Obtiene todos los registros de perfiles por estado

from opticall.src.modules.auth.domain.entities.profile import Perfiles
from opticall.src.modules.auth.domain.repositories.profile_repository import ProfileRepository
from opticall.src.shared.services.database import get_db
from typing import List

class ListarPerfilesByEstadoUseCase:
    """
    Caso de uso para obtener una lista de perfiles según su estado (activo o inactivo).
    """
    def __init__(self, profile_repository: ProfileRepository):
        """
        Inicializa el caso de uso.

        Args:
            profile_repository: Repositorio de perfiles.
        """
        self.profile_repository = profile_repository

    def execute(self, active: bool) -> List[Perfiles]:
        """
        Obtiene una lista de perfiles según su estado.

        Args:
            active: True para perfiles activos, False para perfiles inactivos.

        Returns:
            Una lista de objetos Profile.
        """
        return self.profile_repository.get_by_status(active)
