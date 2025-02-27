#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     api/auth
# @subpackage  autenticacion
# @file        login_route
# @Date        2025-02-26 21:22:32
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Implementa la ruta de autenticación de usuario

from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from opticall.src.modules.auth.application.autenticacion.autenticar_usuario_use_case import AutenticarUsuarioUseCase
from opticall.src.modules.auth.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from opticall.src.shared.services.database import get_db
# from opticall.src.modules.auth.domain.entities.user import User

# from opticall.src.modules.auth.application.gestion_perfiles.listar_perfiles_by_estado import ListarPerfilesByEstadoUseCase
# from opticall.src.modules.auth.infrastructure.repositories.sqlalchemy_profile_repository import SqlAlchemyProfileRepository
# from opticall.src.shared.services.database import get_db
# from opticall.src.modules.auth.domain.entities.profile import Perfiles
# from typing import List
# from opticall.src.modules.auth.domain.value_objects.estado_value_object import EstadoValueObject

auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user_repository = SqlAlchemyUserRepository(next(get_db()))
    autenticar_usuario_use_case = AutenticarUsuarioUseCase(user_repository)
    try:
        user = autenticar_usuario_use_case.execute(email, password)
        if not user:
            return jsonify({'error': 'Credenciales inválidas'}), 403
        login_user(user)
        return jsonify({'message': 'Usuario autenticado'})
    except Exception as e:
        # Reemplaza con un logger adecuado
        print(f"Error al autenticar usuario: {e}")
        return jsonify({'error': f"Error al autenticar usuario {e}"}), 500



# @auth_bp.route('/profile')
# def listar_perfiles():
#     estado = 'Activo'  # request.args.get('estado')
#     if estado.lower() == 'activo':
#         active = True
#     elif estado.lower() == 'inactivo':
#         active = False
#     else:
#         return jsonify({'error': 'El estado debe ser activo o inactivo'}), 400
#     profile_repository = SqlAlchemyProfileRepository(next(get_db()))
#     listar_perfiles_use_case = ListarPerfilesByEstadoUseCase(
#         profile_repository)
#     try:
#         perfiles = listar_perfiles_use_case.execute(active)
#         if not perfiles:
#             return jsonify({'error': 'No se encontraron perfiles'}), 403
#         perfiles_data = []
#         for perfil in perfiles:
#             perfiles_data.append({
#                 'id': perfil.id,
#                 'nombre': perfil.nombre,
#                 'descripcion': perfil.descripcion,
#                 'estado': perfil.estado
#             })
#         return jsonify(perfiles_data)
#     except Exception as e:
#         # Reemplaza con un logger adecuado
#         print(f"Error al listar perfiles: {e}")
#         return jsonify({'error': f"Error al listar perfiles {e}"}), 500
