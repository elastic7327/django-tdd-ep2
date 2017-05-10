#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from django.http import Http404
from django.test import RequestFactory
from mixer.backend.django import mixer

from birdie import forms

pytestmark = pytest.mark.django_db

class TestPostForm:
    def test_form(self):
        form = forms.PostForm(data={})
        assert form.is_valid() == False, 'Should be invalid if no data given'

        form = forms.PostForm(data={'body':'World'})
        assert form.is_valid() == False, 'Should be invalid if too short'
        assert 'body' in form.errors, 'Should have body field error'

        form = forms.PostForm(data={'body':'World!!!!!'})
        assert form.is_valid() == True, 'Should be valid if long enough'


