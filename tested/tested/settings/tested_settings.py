#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME'  : ':memory:',
        'NAME': os.path.join(BASE_DIR, '../../databases/db.sqlite3'),
    }
}

#EMAIL_BACKEND = 'django.core.mail.backend.loceme.EmailBackend'
