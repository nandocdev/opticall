#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     OptiCall/opticall
# @subpackage  config
# @file        config
# @Date        2025-02-25 15:31:41
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

import os
import logging
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Clase base para la configuración de la aplicación.
    """
    # General
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Database Configuration
    DB_DRIVER = os.getenv("DB_DRIVER", "mysql")
    # Sin valor por defecto, para forzar la configuración
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")  # Sin valor por defecto
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    # Convertir a entero inmediatamente
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "opticall_db")

    # Construct SQLAlchemy Database URI
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        """
        Construye la URI de la base de datos SQLAlchemy.
        """
        if not all([self.DB_DRIVER, self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_PORT, self.DB_NAME]):
            raise ValueError(
                "Faltan variables de entorno para la configuración de la base de datos.")

        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    # Imprime el valor de LOG_LEVEL

    # Validar el nivel de log
    try:
        LOGGING_LEVEL = getattr(logging, LOG_LEVEL)
    except AttributeError:
        LOGGING_LEVEL = logging.INFO
        print(f"Nivel de log inválido '{LOG_LEVEL}'. Usando INFO por defecto.")

    # Add a method to check all required environment variables
    @staticmethod
    def check_required_variables(required_variables):
        missing_variables = [
            var for var in required_variables if not os.getenv(var)]
        if missing_variables:
            raise ValueError(
                f"Faltan las siguientes variables de entorno requeridas: {', '.join(missing_variables)}")


class DevelopmentConfig(Config):
    """
    Configuración para el entorno de desarrollo.
    """
    DEBUG = True
    LOG_LEVEL = "DEBUG"  # Más detalles en los logs de desarrollo
    # SQLALCHEMY_ECHO = True # Uncomment to see SQL queries
    # For development you may want to set default values that are safe for development
    DB_USER = os.getenv("DB_USER", "dev_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "dev_password")


class ProductionConfig(Config):
    """
    Configuración para el entorno de producción.
    """
    DEBUG = False
    # Force HTTPS
    # SESSION_COOKIE_SECURE = True
    # REMEMBER_COOKIE_SECURE = True
    # PREFERRED_URL_SCHEME = 'https'
    # Strict security headers
    # SECURITY_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURITY_HSTS_PRELOAD = True

# Example Usage:
# config = Config()
# print(config.SQLALCHEMY_DATABASE_URI) # Access URI via property
