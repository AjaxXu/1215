#!/usr/bin/env python
# encoding: utf-8

import hashlib
from datetime import datetime

from werkzeug import cached_property

from flask import abort, current_app
from flask.ext.sqlalchemy import BaseQuery
from flask.ext.principal import RoleNeed, UserNeed, Permission

from blog import db

class UserQuery(BaseQuery):

    def from_identity(self, identity):
        try:
            user = self.get(int(identity.name))
        except ValueError:
            user = None

        if user:
            identity.provides.update(user.provides)

        identity.user = user
        return user

    def authenticate(self, login, password):

        user = self.filter(db.or_(User.username==login,
                                  User.email==login)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated

    def search(self, key):
        query = self.filter(db.or_(User.email==key,
                                   User.nickname.ilike('%'+key+'%'),
                                   User.username.ilike('%'+key+'%')))

        return query

    def get_by_username(self, username):
        user = self.filter(User.username==username).first()
        if user is None:
            abort(404)
        return user

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password= hashlib.md5(password)  #呵呵，这样在插入数据自动给密码哈希了

    def __repr__(self):
        return "<User '{:s}'>".format(self.username)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = hashlib.md5(password).hexdigest()

    password = db.synonym("_password",
                          descriptor=property(_get_password,
                                              _set_password))

    def check_password(self,password):
        if self.password is None:
            return False
        return self.password == hashlib.md5(password).hexdigest()