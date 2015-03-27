#!/usr/bin/env python

from elixir import *

class Photo(Entity):
    
    using_options(tablename = 'photo')
    
    name = Field(String(50))
    address = Field(String(150))
    info = Field(String(300), default='nn')
    keywords = ManyToMany('Keyword')
    person = ManyToOne('Person')
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address
        
    def getInfo(self):
        return self.info
    
    def setInfo(self, info):
        self.info = info
    
    def getKeywords(self):
        return self.keywords
    
    def setKeywords(self, keywords):
        self.keywords = keywords
    
    def getPerson(self):
        return self.person
    
    def setPerson(self, person):
        self.person = person
    
    def __repr__(self):
        return "<Photo('%s','%s')>" % (self.name, self.address)