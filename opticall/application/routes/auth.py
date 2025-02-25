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

from flask import Blueprint, render_template, redirect, url_for, request, flash


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