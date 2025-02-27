#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/domain
# @subpackage  value_objects
# @file        estado_value_object
# @Date        2025-02-26 15:44:21
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description Objeto de valor para el estado, que puede ser activo o inactivo., se almacena en booleano


class EstadoValueObject:
    """Objeto de valor para el estado, que puede ser activo o inactivo."""
    def __init__(self, estado: bool = True):
        """
        Inicializa el objeto de valor.

        Args:
            estado: True para activo, False para inactivo.
        """
        self._estado = estado

    @property
    def estado(self) -> bool:
        """Devuelve el estado."""
        return self._estado

    def __eq__(self, other):
        """Compara dos objetos EstadoValueObject por su estado."""
        if isinstance(other, EstadoValueObject):
            return self._estado == other._estado
        return False

    def __repr__(self):
        return f"<EstadoValueObject {self._estado}>"