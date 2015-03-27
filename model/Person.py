#!/usr/bin/env python

from elixir import *

class Person(Entity):
    
    using_options(tablename = 'person')
    
    name = Field(String(100))
    last = Field(String(100))
    email = Field(String(50))
    position = Field(String(50))
    position_long = Field(String(200))
    phone = Field(String(20))
    photos = OneToMany('Photo')
    projects = ManyToMany('Project')
    researcharea = ManyToOne('ResearchArea')
    ubication = ManyToOne('Ubication')
    department = ManyToOne('Department')
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def getLast(self):
        return self.last
    
    def setLast(self, last):
        self.last = last
    
    def getFullName(self):
        return self.name + ' ' + self.last
        
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
        
    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position
    
    def getPhone(self):
        return self.phone
    
    def setPhone(self, phone):
        self.phone = phone
        
    def getPhotos(self):
        return self.photos
    
    def setPhotos(self, photos):
        self.photos = photos
        
    def getResearchArea(self):
        return self.researcharea
    
    def setResearchArea(self, researcharea):
        self.researcharea = researcharea
    
    def getProjects(self):
        return self.projects
    
    def setProjects(self, projects):
        self.projects = projects
        
    def getDepartment(self):
        return self.department
    
    def setDepartment(self, department):
        self.department = department
        
    def getUbication(self):
        return self.ubication
    
    def setUbication(self, ubication):
        self.ubication = ubication
    
    def __repr__(self):
        return "<Person('%s','%s', '%s', '%s')>" % (self.name, self.last, self.email, self.position)