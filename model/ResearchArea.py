#!/usr/bin/env python

from elixir import *

class ResearchArea(Entity):
    
    using_options(tablename = 'research_area')

    name = Field(String(100))
    description = Field(String(500))
    alias = Field(String(100))
    persons = OneToMany('Person')

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getDescription(self):
        return self.description
    
    def setDescription(self, desc):
        self.description = desc
        
    def getAlias(self):
        return self.alias
    
    def setAlias(self, alias):
        self.alias = alias
        
    def getPersons(self):
        return self.persons
    
    def setPersons(self, persons):
        self.persons = persons
        
    def __repr__(self):
        return "<Research Area('%s','%s','%s')>" % (self.name, self.description, self.alias)
