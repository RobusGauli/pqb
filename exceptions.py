__author__ = 'robusgauli@gmail.com'
import sys
import os


class BadQueryException(Exception):
    '''Custom Exception thrown when you have a bad query'''
    def __init__(self, value):
        super().__init__(value)