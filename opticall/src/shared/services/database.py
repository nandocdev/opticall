#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     src/shared
# @subpackage  services
# @file        database
# @Date        2025-02-25 22:55:32
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description clase de implementacion de base de datos con sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from opticall.config.config import Config

config = Config()

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URL = config.get('database', 'url')
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)

def drop_db():
    Base.metadata.drop_all(bind=engine)

