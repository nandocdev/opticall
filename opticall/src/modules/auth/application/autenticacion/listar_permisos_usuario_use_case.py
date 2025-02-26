#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  autenticacion
# @file        listar_permisos_usuario_use_case
# @Date        2025-02-26 11:21:51
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Caso de uso que permite listar los permisos de un usuario basado en el perfil del mismo

from opticall.src.modules.auth.domain.repositories.permission_repository import PermisoRepository
from opticall.src.modules.auth.domain.entities.permission import Permiso
from opticall.src.modules.auth.application.exceptions import NoPremissionAsignedError

class ListarPermisosUsuarioUseCase:
    def __init__(self, permiso_repository: PermisoRepository):
        self.permiso_repository = permiso_repository

    def execute(self, perfil: int) -> Permiso:
        try:
            permisos = self.permiso_repository.get_by_profile(perfil)
        except NoPremissionAsignedError as e:
            raise e
        except Exception as e:
            raise e
        
        return permisos


