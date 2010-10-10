#!/usr/bin/env python
# -*- coding:utf-8 -*-

class JString(object):

    def __init__(self, str=''):
        self.value = str

    def __str__(self):
        return self.value

    def charAt(self, index):
        return self.value[index]

    def codePointAt(self, index):
        return ord(self.value[index])

    def codePointBefore(self, index):
        return self.codePointAt(index - 1)

    def codePointCount(self, beginIndex, endIndex):
        return len(self.value[beginIndex:endIndex])
