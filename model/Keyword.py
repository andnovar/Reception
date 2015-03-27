#!/usr/bin/env python

from elixir import *

class Keyword(Entity):
    
    using_options(tablename = 'keyword')
    
    word = Field(String(30))
    level = Field(Integer)
    cont = Field(Integer, default=0)
    photos = ManyToMany('Photo')
    projects = ManyToMany('Project')
    
    def getWord(self):
        return self.word

    def setWord(self, word):
        self.word = word
    
    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level
        
    def getCont(self):
        return self.cont
    
    def setCont(self, cont):
        self.cont = cont
        
    def getPhotos(self):
        return self.photos
    
    def setPhotos(self, photos):
        self.photos = photos
        
    def getProjects(self):
        return self.projects
    
    def setProjects(self, projects):
        self.projects = projects
        
    def __repr__(self):
        return "<Keyword('%s','%s', '%s')>" % (self.word, self.level, self.cont)