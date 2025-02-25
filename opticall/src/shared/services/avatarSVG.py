#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     src/shared
# @subpackage  services
# @file        avatarSVG
# @Date        2025-02-25 13:56:58
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description basado en el nombre y apellido genera una imagen SVG utilizando las iniciales

import random


class AvatarSVG:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.width = 100
        self.height = 100
        self.bgcolor = f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"
        self.textcolor = "white"
        self.text = f"{name[0]}{lastname[0]}".upper()

    def generate(self):
        # agrega texto en bold y en mayusculas
        image =  f'''<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">
            <rect width="100%" height="100%" fill="{self.bgcolor}"/>
            <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="{self.textcolor}" font-size="40" font-family="Arial" font-weight="bold" >{self.text}</text>
        </svg>'''.strip().encode()
        # contiene un string con el SVG, imagen}
        return image

