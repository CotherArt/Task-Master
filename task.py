# coding: utf-8
__author__ = 'CotherArt'


class Task:

    def __init__(self, name):
        self.name = name
        self.check = False

    def do(self):
        self.check = True

    def undo(self):
        self.check = False

    def ischeck(self):
        return self.check
