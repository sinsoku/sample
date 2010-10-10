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

    def test_codePointBefore(self):
        jstr = JString(u'0z?!あ表');
        eq_(jstr.codePointBefore(1), 48)
        eq_(jstr.codePointBefore(2), 122)
        eq_(jstr.codePointBefore(3), 63)
        eq_(jstr.codePointBefore(4), 33)
        eq_(jstr.codePointBefore(5), 12354)
        eq_(jstr.codePointBefore(6), 34920)

    def test_codePointCount(self):
        jstr = JString(u'0z?!あ表');
        eq_(jstr.codePointCount(0, 0), 0)
        eq_(jstr.codePointCount(0, 1), 1)
        eq_(jstr.codePointCount(0, 2), 2)
        eq_(jstr.codePointCount(0, 3), 3)
        eq_(jstr.codePointCount(0, 4), 4)
        eq_(jstr.codePointCount(0, 5), 5)

    def test_getChars(self):
        eq_(JString('abc').getChars(0, 2, '012345', 2), '01ab45')

    def test_getBytes(self):
        eq_(JString(u'0z?!あ表').getBytes(), [48, 122, 63, 33, 12354, 34920])
        eq_(JString(u'abc').getBytes(), [97, 98, 99])

    def test_equals(self):
        ok_(JString('abc').equals('abc'))
        ok_(not JString('abc').equals('abcd'))
        ok_(JString(u'abcあ表').equals(u'abcあ表'))
        ok_(not JString(u'abcあ表').equals(u'abcあ表d'))

    def test_equalsIgnoreCase(self):
        ok_(JString('abc').equalsIgnoreCase('ABC'))
        ok_(JString('aBc').equalsIgnoreCase('AbC'))
        ok_(not JString('aBc').equalsIgnoreCase('aBcD'))

    def test_compareTo(self):
        jstr = JString('abc')
        eq_(jstr.compareTo('abc'), 0)
        eq_(jstr.compareTo('aac'), 1)
        eq_(jstr.compareTo('acc'), -1)

        # 文字列の長さが異なるパターン
        eq_(jstr.compareTo('ab'), 1)
        eq_(jstr.compareTo('abcdef'), -3)
