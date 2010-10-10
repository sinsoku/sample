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

    def test_init_JString_ustr(self):
        eq_(str(JString(u'')), '')
        eq_(str(JString(u'abc')), 'abc')
