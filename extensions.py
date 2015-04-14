#!/usr/bin/env python
#coding=utf-8

from flask.ext.mail import Mail
from flask.ext.cache import Cache
from flask.ext.uploads import UploadSet, IMAGES

__all__ = ['mail', 'cache', 'photos']

mail = Mail()
cache = Cache()
photos = UploadSet('photos', IMAGES)