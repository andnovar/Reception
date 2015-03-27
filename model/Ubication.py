#!/usr/bin/env python

from elixir import *

class Ubication(Entity):
    
    using_options(tablename = 'ubication')

    building = Field(String(100))
    name = Field(String(100))
    x = Field(Integer)
    y = Field(Integer)
    persons = OneToMany('Person')
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y
    
    def __repr__(self):
        return "<Ubication('%s','%s','%s')>" % (self.name, self.x, self.y)