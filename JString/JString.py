#!/usr/bin/env python
# -*- coding:utf-8 -*-

class JString(object):

    def __init__(self, str=''):
        self.str = str

    def __str__(self):
        return self.str

    def charAt(self, index):
        return self.str[index]

    def codePointAt(self, index):
        return ord(self.str[index])

    def codePointBefore(self, index):
        return self.codePointAt(index - 1)
