# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your models here.
class TopicList:
    def __init__(self):
        pass

    @staticmethod
    def is_addition(name):
        if not isinstance(name, basestring):
            return False

        return "ADDITION" == name.upper()


    @staticmethod
    def is_subtraction(name):
        if not isinstance(name, basestring):
            return False

        return "SUBTRACTION" == name.upper()

    @staticmethod
    def is_multiplication(name):
        if not isinstance(name, basestring):
            return False

        return "MULTIPLICATION" == name.upper()
    @staticmethod
    def is_division(name):
        if not isinstance(name, basestring):
            return False

        return "DIVISION" == name.upper()

