#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        auth
# @Date        2025-02-25 10:58:35
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
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


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('/login.html')

@auth.route('/register')
def register():
    return render_template('/register.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

@auth.route('/forgot-password')
def forgot_password():
    return render_template('/forgot-password.html')

@auth.route('/reset-password')
def reset_password():
    return render_template('/reset-password.html')

@auth.route('/users')
def users():
    return render_template('/users.html')

@auth.route('/users/<id>')
def user(id):
    return render_template('/user.html')