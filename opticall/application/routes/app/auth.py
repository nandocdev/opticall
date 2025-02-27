#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        auth
# @Date        2025-02-25 10:58:35
# @auth_bpor      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Rutas que generan vistas de autenticación y autorización de usuarios
"""
    ## **🔐 auth.py** (Autenticación y autorización)
    | Método | Ruta | Descripción |
    |--------|------|-------------|
    | `GET`  | `/login` | Muestra el formulario de inicio de sesión |
    | `GET`  | `/register` | Muestra el formulario de registro de usuario |
    | `GET`  | `/logout` | Cierra la sesión del usuario |
    | `GET`  | `/forgot-password` | Muestra el formulario para recuperar contraseña |
    | `GET`  | `/reset-password` | Muestra la página para resetear contraseña |
    | `GET`  | `/users` | Lista de usuarios y roles |
    | `GET`  | `/users/<id>` | Detalles de un usuario |
"""

import json
from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash
from opticall.src.modules.auth.application.gestion_perfiles.listar_perfiles_by_estado import ListarPerfilesByEstadoUseCase
from opticall.src.modules.auth.infrastructure.repositories.sqlalchemy_profile_repository import SqlAlchemyProfileRepository
from opticall.src.shared.services.database import get_db
from opticall.src.modules.auth.domain.entities.profile import Perfiles
from typing import List
from opticall.src.modules.auth.domain.value_objects.estado_value_object import EstadoValueObject

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/register')
def register():
    return render_template('auth/register.html')

@auth_bp.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

@auth_bp.route('/forgot-password')
def forgot_password():
    return render_template('auth/forgot-password.html')

@auth_bp.route('/reset-password')
def reset_password():
    return render_template('auth/reset-password.html')

@auth_bp.route('/users')
def users():
    return render_template('auth/users.html')

@auth_bp.route('/users/<id>')
def user(id):
    return render_template('auth/user.html')

@auth_bp.route('/profile')
def listar_perfiles():
    estado = 'Activo' # request.args.get('estado')
    if estado.lower() == 'activo':
        active = True
    elif estado.lower() == 'inactivo':
        active = False
    else:
        return jsonify({'error': 'El estado debe ser activo o inactivo'}), 400
    profile_repository = SqlAlchemyProfileRepository(next(get_db()))
    listar_perfiles_use_case = ListarPerfilesByEstadoUseCase(profile_repository)
    try:
        perfiles = listar_perfiles_use_case.execute(active)
        if not perfiles:
            return jsonify({'error': 'No se encontraron perfiles'}), 403
        perfiles_data = []
        for perfil in perfiles:
            perfiles_data.append({
                'id': perfil.id,
                'nombre': perfil.nombre,
                'descripcion': perfil.descripcion,
                'estado': perfil.estado
            })
        return jsonify(perfiles_data)
    except Exception as e:
        # Reemplaza con un logger adecuado
        print(f"Error al listar perfiles: {e}")
        return jsonify({'error': f"Error al listar perfiles {e}"}), 500
