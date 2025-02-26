#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/infrastructure
# @subpackage  repositories
# @file        sqlalchemy_user_repository
# @Date        2025-02-25 23:25:32
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 


from opticall.src.modules.auth.domain.entities.user import Usuarios
from opticall.src.modules.auth.domain.repositories.user_repository import UserRepository
import bcrypt

class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session):
        self.session = session

    def create(self, user: Usuarios):
        self.session.add(user)
        self.session.commit()

    def get_by_username(self, username: str) -> Usuarios:
        return self.session.query(Usuarios).filter(Usuarios.username == username).first()

    def get_by_id(self, id: int) -> Usuarios:
        return self.session.query(Usuarios).filter(Usuarios.id == id).first()

    def get_all(self):
        return self.session.query(Usuarios).all()

    def update(self, user: Usuarios):
        self.session.add(user)
        self.session.commit()

    def delete(self, user: Usuarios):
        self.session.delete(user)
        self.session.commit()

    def get_by_email(self, email: str) -> Usuarios:
        return self.session.query(Usuarios).filter(Usuarios.email == email).first()

    def get_by_username_and_password(self, username: str, password: str) -> Usuarios:
        user = self.session.query(Usuarios).filter(Usuarios.username == username).first()
        if user is None:
            return None
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return user
        return None

    def get_by_email_and_password(self, email: str, password: str) -> Usuarios:
        user = self.session.query(Usuarios).filter(Usuarios.email == email).first()
        if user is None:
            return None
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return user
        return None

    def get_by_username_or_email(self, username: str, email: str) -> Usuarios:
        return self.session.query(Usuarios).filter((Usuarios.username == username) | (Usuarios.email == email)).first()

    def get_by_username_or_email_and_password(self, username: str, email: str, password: str) -> Usuarios:
        user = self.session.query(Usuarios).filter((Usuarios.username == username) | (Usuarios.email == email)).first()
        if user is None:
            return None
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return user
        return None