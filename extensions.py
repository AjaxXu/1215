#!/usr/bin/env python
#coding=utf-8

from flask_mail import Mail
from flask_cache import Cache
from flaskext.uploads import UploadSet, IMAGES

__all__ = ['mail', 'cache', 'photos']

mail = Mail()
cache = Cache()
photos = UploadSet('photos', IMAGES)