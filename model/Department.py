#!/usr/bin/env python

from elixir import *

class Department(Entity):
    using_options(tablename = 'department')

    alias = Field(String(50))
    name = Field(String(100))
    description = Field(String(400))
    persons = OneToMany('Person')
    
    def getAlias(self):
        return self.alias
    
    def setAlias(self, alias):
        self.alias = alias
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getDescription(self):
        return self.description
    
    def setDescription(self, desc):
        self.description = desc
    
    def __repr__(self):
        return "<Department('%s','%s', '%s')>" % (self.alias, self.name, self.description)