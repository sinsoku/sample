#!/usr/bin/env python
# -*- coding:utf-8 -*-

from nose.tools import *
from JString import JString

class TestJString(object):

    def test_init_JString(self):
        eq_(str(JString()), '')

    def test_init_JString_str(self):
        eq_(str(JString('')), '')
        eq_(str(JString('abc')), 'abc')
        eq_(str(JString('あ')), 'あ')

    def test_init_JString_ustr(self):
        eq_(unicode(JString(u'')), u'')
        eq_(unicode(JString(u'abc')), u'abc')
        eq_(unicode(JString(u'あ')), u'あ')

    def test_charAt(self):
        jstr = JString('abc')
        eq_(jstr.charAt(0), 'a')
        eq_(jstr.charAt(1), 'b')
        eq_(jstr.charAt(2), 'c')

    def test_codePointAt(self):
        jstr = JString(u'0z?!あ表');
        eq_(jstr.codePointAt(0), 48)
        eq_(jstr.codePointAt(1), 122)
        eq_(jstr.codePointAt(2), 63)
        eq_(jstr.codePointAt(3), 33)
        eq_(jstr.codePointAt(4), 12354)
        eq_(jstr.codePointAt(5), 34920)
