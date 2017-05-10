#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from birdie import views

from django.http import Http404
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

class TestHomeView():
    def test_anonymous(self):
        req = RequestFactory().get('/')

        # 사실 팩토리라는 방법을 사용하게되면, self.client.get() 이렇게
        # 미들웨어를 거치고나서 뭔가가 발생하는 것이 아니라.
        # 그냥 테스트를 통과 했는지, 정말 두리뭉실하게 테스트를 패스하게된다.
        # 사실 이전에, 템플릿은 위 처럼, self.client.get() or post() .. patch()
        # 등으로 테스트가 완료 되어져야한다.
        # Factory() does NOT render the view and test the template
        # Factory() does NOT call 'urls.py'

        response = views.HomeView.as_view()(req)

        assert response.status_code == 200

class TestAdminView():
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = views.AdminView.as_view()(req)
        # assert resp.status_code == 302
        # assert '/account/login/?next=/' in resp.url
        assert '/login/' in resp.url, 'Should be redirect to login'

    def test_superuser(self):
        user = mixer.blend('auth.User', is_superuser=True)
        req = RequestFactory().get('/')
        req.user = user
        resp = views.AdminView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by superuser'

class TestPostUpdateView():
    def test_get(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        obj = mixer.blend('birdie.Post')
        resp = views.PostUpdateView.as_view()(req, pk=obj.pk)
        assert resp.status_code == 200, 'Should be callable by anyone else'

    def test_post(self):
        post = mixer.blend('birdie.Post')
        data = {'body': 'New Body Text!!'}
        req = RequestFactory().post('/', data=data)
        req.user = AnonymousUser()
        resp = views.PostUpdateView.as_view()(req, pk=post.pk)
        assert resp.status_code == 302, 'Should redirect to success view'
        post.refresh_from_db()
        assert post.body == 'New Body Text!!', 'Should update the post'

    def test_security(self):
        user = mixer.blend('auth.User', first_name='Daniel')
        post = mixer.blend('birdie.Post')
        req = RequestFactory().post('/', data={})
        req.user = user
        with pytest.raises(Http404):
            views.PostUpdateView.as_view()(req, pk=post.pk)
