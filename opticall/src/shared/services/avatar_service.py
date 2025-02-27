#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     src/shared
# @subpackage  services
# @file        avatar_service
# @Date        2025-02-27 09:42:30
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

import random

class AvatarService:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.width = 100
        self.height = 100
        self.fontsize = self._calculate_font_size()
        self.bgcolor = self._generate_bgcolor()
        self.textcolor = self._calculate_text_color()
        self.text = f"{name[0]}{lastname[0]}".upper()

    def generate(self):
        # agrega texto en bold y en mayusculas
        image = f'''<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">
            <rect width="100%" height="100%" fill="{self.bgcolor}"/>
            <text x="{self._txt_x_position()}" y="{self._txt_y_position()}" dominant-baseline="middle" text-anchor="middle" fill="{self.textcolor}" font-size="{self.fontsize}" font-family="Arial" font-weight="bold" >{self.text}</text>
        </svg>'''.strip().encode()
        return image
    
    # calcula el tamaño de la fuente en base al tamaño de la imagen
    def _calculate_font_size(self):
        return self.width * 0.56
    
    def _txt_x_position(self):
        return self.width * 0.55
    
    def _txt_y_position(self):
        return self.height * 0.55
    
    # define el color del texto en base al color de fondo
    def _calculate_text_color(self):
        r, g, b = self._generate_rgb()
        luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
        return "black" if luma < 128 else "white"
    
    # genera el color de fondo aleatorio
    def _generate_rgb(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b
    
    # genera el color de fondo aleatorio
    def _generate_bgcolor(self):
        color = self._generate_rgb()
        return f"rgb{color}"
    
