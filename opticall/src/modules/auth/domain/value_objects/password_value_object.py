#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/domain
# @subpackage  value_objects
# @file        password_value_object
# @Date        2025-02-25 23:10:45
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description ValueObject de password, se encarga de encriptar la contraseña

import bcrypt


class Password:
    MIN_LENGTH = 8  # Mínimo de 8 caracteres

    def __init__(self, raw_password: str, hashed_password: str = None):
        """
        Si se pasa raw_password, se valida y hashea.
        Si se pasa hashed_password, se usa directamente (por ejemplo, al cargar desde BD).
        """
        if raw_password:
            self._validate(raw_password)
            self._hashed_password = self._hash_password(raw_password)
        elif hashed_password:
            self._hashed_password = hashed_password
        else:
            raise ValueError(
                "Debe proporcionar una contraseña en texto plano o un hash.")

    @staticmethod
    def _hash_password(password: str) -> str:
        """Genera un hash seguro para la contraseña usando bcrypt."""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def _validate(password: str):
        """Valida las reglas de negocio para la contraseña."""
        if len(password) < Password.MIN_LENGTH:
            raise ValueError(
                f"La contraseña debe tener al menos {Password.MIN_LENGTH} caracteres.")

    def verify(self, raw_password: str) -> bool:
        """Verifica si una contraseña en texto plano coincide con el hash almacenado."""
        return bcrypt.checkpw(raw_password.encode(), self._hashed_password.encode())

    @property
    def hashed(self) -> str:
        """Devuelve el hash de la contraseña (para almacenamiento)."""
        return self._hashed_password

    def __eq__(self, other):
        """Compara dos objetos Password por su hash."""
        if isinstance(other, Password):
            return self._hashed_password == other._hashed_password
        return False

    def __repr__(self):
        return "<Password (hash oculto)>"
