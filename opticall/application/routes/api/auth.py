#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     application/routes
# @subpackage  api
# @file        auth
# @Date        2025-02-26 16:16:13
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash

from opticall.application.routes.app.auth import users

# usuarios
users_api = Blueprint('api_users', __name__)


# perfiles
profile_api = Blueprint('api_profiles', __name__)
# roles

roles_api = Blueprint('api_roles', __name__)

@roles_api.route('/roles', methods=['GET'])
def get_roles():
    return jsonify({"message": "List of roles"})
    
@roles_api.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    return jsonify({"message": f"Details for role with ID {role_id}"})

@roles_api.route('/roles', methods=['POST'])
def create_role():
    new_role = request.json.get('role', '')

    return jsonify({"message": "Role created", "role": new_role}), 201

@roles_api.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    updated_role = request.json.get('role', '')
    return jsonify({"message": f"Role with ID {role_id} updated", "role": updated_role})

# permisos
premissions_api = Blueprint('api_permissions', __name__)