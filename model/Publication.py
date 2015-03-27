#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Publication(Base):
    
    __tablename__ = 'publication'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    year = Column(String)
    description = Column(String)
    
    def __init__(self, name, year, desc):
        self.name = name
        self.year = year
        self.description = desc
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getYear(self):
        return self.year
    
    def setYear(self, year):
        self.year = year

    def getDescription(self):
        return self.description

    def setDescription(self, desc):
        self.description = desc
    
    def __repr__(self):
        return "<Publication('%s','%s','%s')>" % (self.name, self.year, self.description)