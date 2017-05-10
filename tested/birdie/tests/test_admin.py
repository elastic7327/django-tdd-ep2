#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_admin.py

import pytest

from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

from birdie import admin
from birdie import models

class TestPostAdmin:
    def test_excerot(self):
        obj = mixer.blend('birdie.Post')
        site = AdminSite()
        post_admin = admin.PostAdmin(models.Post, site)

        obj = mixer.blend('birdie.Post', body='Hello World')
        res = post_admin.excerpt(obj)
        assert res == 'Hello', 'Should return first few characters'
