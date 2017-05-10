#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_admin.py

import pytest

from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

from birdie.models import Post
from birdie.admin import admin

class TestPostAdmin:
    def test_excerot(self):
        obj = mixer.blend('birdie.Post')
        assert 1 is 1
