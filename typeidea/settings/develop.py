#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: NOQA
# @Time    : 2019-03-06 13:44
# @Author  : lamber
# @Site    : dcgamer.top
# @File    : develop.py
# @Software: PyCharm
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

