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
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from typing import Generator
from opticall.config.config import Config


config = Config()
SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    Base.metadata.create_all(bind=engine)
    engine.connect()
    print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
    raise


# Dependency Injection
def get_db() -> Generator[Session, None, None]:
    """
    Dependency to inject the database session into routes and other functions.
    Ensures proper management of session lifecycle.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@contextmanager
def get_session() -> Generator[Session, None, None]:
    """
    Provides a transactional scope around a series of operations.
    """
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(f"Error en la sesion, rollback: {e}")
        session.rollback()
        raise
    finally:
        session.close()
