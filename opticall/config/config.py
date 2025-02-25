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
    db_driver = os.getenv("DB_DRIVER", "mysql")
    db_user = os.getenv("DB_USER", "desarrollo")
    db_password = os.getenv("DB_PASSWORD", "1q2w3e4r5t")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "opticall_db")
    db_url = f"{db_driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def get_db_uri(cls):
        return cls.SQLALCHEMY_DATABASE_URI

    @classmethod
    def get_config_summary(cls):
        return {
            "db_driver": cls.db_driver,
            "db_user": cls.db_user,
            "db_host": cls.db_host,
            "db_port": cls.db_port,
            "db_name": cls.db_name
        }
    