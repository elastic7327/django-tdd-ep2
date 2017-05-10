#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_models.py

import pytest

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestPostModel:

    def test_model(self):
        obj = mixer.blend('birdie.Post')
        assert obj.pk == 1, 'Should create a Post instance'

    def test_get_excerpt(self):
        obj = mixer.blend('birdie.Post', body='Hello World')
        res = obj.get_excerpt(5)
        assert res == 'Hello', 'Should return first few characters'
