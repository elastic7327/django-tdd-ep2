#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from birdie.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', )

    # 재미있는 규칙이다, 모든 필드 앞에 clean이라는게 붙는데, 
    # 아래 함수의 뜻은 body에 관해서 validation을 제정의 하겠다는 뜻이다.
    def clean_body(self):
        # clean_data라는것은 장고 컨벤션에서 소개가 되는 것이므로, 
        # 공식홈페이지에 가서 확인 해보자
        data = self.cleaned_data.get('body')
        if len(data) <= 5:
            raise forms.ValidationError('Message is too short')
        return data
