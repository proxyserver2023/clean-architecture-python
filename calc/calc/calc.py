# -*- coding: utf-8 -*-

class Calc:
    def add(self, *args):
        sum = 0
        for arg in args:
            sum += arg
        return sum
