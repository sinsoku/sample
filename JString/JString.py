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

    def getChars(self, srcBegin, srcEnd, dst, dstBegin):
        return dst[0:dstBegin] + self.value[srcBegin:srcEnd] + dst[dstBegin + srcEnd - srcBegin:]

    def getBytes(self):
        return [ord(x) for x in self.value]

    def equals(self, str):
        return self.value == str

    def equalsIgnoreCase(self, str):
        return self.value.lower() == str.lower()

    def compareTo(self, anotherString):
        length = len(self.value) - len(anotherString)
        if length != 0:
            return length
        else:
            for n in range(len(self.value)):
                length = ord(self.value[n]) - ord(anotherString[n])
                if length != 0:
                    return length
        return 0

    def startsWith(self, prefix):
        return self.value.startswith(prefix)

    def endsWith(self, suffix):
        return self.value.endswith(suffix)
