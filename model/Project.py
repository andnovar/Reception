#!/usr/bin/env python

from elixir import *

class Project(Entity):

    using_options(tablename = 'project')

    name = Field(String(300))
    description = Field(String(1000))
    doc = Field(String(150))
    persons = ManyToMany('Person')
    keywords = ManyToMany('Keyword')
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDescription(self):
        return self.description

    def setDescription(self, desc):
        self.description = desc
        
    def getDoc(self):
        return self.doc
    
    def setDoc(self, doc):
        self.doc = doc
    
    def getPersons(self):
        return self.persons
    
    def setPersons(self, persons):
        self.persons = persons
    
    def getKeywords(self):
        return self.keywords
    
    def setKeywords(self, keywords):
        self.keywords = keywords
    
    def __repr__(self):
        return "<Project('%s','%s')>" % (self.name, self.description)