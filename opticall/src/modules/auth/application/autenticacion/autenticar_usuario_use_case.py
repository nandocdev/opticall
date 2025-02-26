#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/application
# @subpackage  autenticacion
# @file        autenticar_usuario_use_case
# @Date        2025-02-26 10:52:07
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Caso de uso que autentica un usuario


from opticall.src.modules.auth.domain.repositories.user_repository import UsuarioRepository
from opticall.src.modules.auth.application.exceptions import CredentialsInvalidError, UserNotFoundError
from opticall.src.modules.auth.domain.entities.user import Usuario

class AutenticarUsuarioUseCase:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    def execute(self, username: str, password: str) -> Usuario:
        try:
            usuario = self.usuario_repository.get_by_username(username)
        except UserNotFoundError as e:
            raise e
        except CredentialsInvalidError as e:
            raise e
        except Exception as e:
            raise UserNotFoundError("Error al obtener usuario")
        
        if not usuario.check_password(password):
            raise CredentialsInvalidError("Nombre de usuario o contraseña incorrectos")
        
        if not usuario.is_active:
            raise CredentialsInvalidError("No se ha encontrado un usuario activo con las credenciales proporcionadas")
        
        return usuario


