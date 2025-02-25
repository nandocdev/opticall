#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     opticall/application
# @subpackage  routes
# @file        shared
# @Date        2025-02-25 14:17:19
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

from flask import Blueprint, render_template, redirect, url_for, request, flash, Response
from opticall.src.shared.services.avatarSVG import AvatarSVG

shared_bp = Blueprint('shared', __name__)

@shared_bp.route('/dynamic/avatar')
def dynamic_avatar():
    name = request.args.get('name', 'Fernando')
    lastname = request.args.get('lastname', 'Castillo')
    avatar = AvatarSVG(name, lastname)
    return Response(avatar.generate(), mimetype='image/svg+xml')
