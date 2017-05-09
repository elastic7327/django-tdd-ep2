import pytest

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

class TestPostModel:
    def test_smoke_test(self):
        assert 1 is 2 ,'We expect this fail'

