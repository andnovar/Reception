#!/usr/bin/env python

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:adminadmin@localhost/touchbase')
engine.echo = True

metadata = MetaData()

metadata.bind = engine

research_area_table = Table('research_area', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(150), nullable=False),
    Column('description', String(500)),
    Column('alias', String(100))
)

department_table = Table('department',metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('description', String(250)),
    Column('alias', String(100))
)

ubication_table = Table('ubication',metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('x', Integer),
    Column('y', Integer)
)

project_table = Table('project',metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(150), nullable=False),
    Column('description', String(1000))
)

publication_table = Table('publication',metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(150), nullable=False),
    Column('year', String(4)),
    Column('description',String(1000))
)

photo_table = Table('photo', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('address', String(150)),
    Column('info', String(300))
)

keyword_table = Table('keyword', metadata,
    Column('id', Integer, primary_key=True),
    Column('word', String(30)),
    Column('level', Integer),
    Column('cont', Integer, default=0)
)

person_table = Table('person', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('last', String(100)),
    Column('email', String(100)),
    Column('position', String(50)),
    Column('research_area_id', Integer, ForeignKey("research_area.id")),
    Column('ubication_id', Integer, ForeignKey("ubication.id")),
    Column('department_id', Integer, ForeignKey("department.id"))
)

photoset_table = Table('photoset',metadata,
    Column('photo_id', Integer, ForeignKey('photo.id')),
    Column('person_id', Integer, ForeignKey('person.id'))
)

memproj_table = Table('memproj', metadata,
    Column('person_id', Integer, ForeignKey('person.id')),
    Column('project_id', Integer, ForeignKey('project.id'))
)

mempub_table = Table('mempub', metadata,
    Column('person_id', Integer, ForeignKey('person.id')),
    Column('publication_id', Integer, ForeignKey('publication.id'))
)

keywordset_table = Table('keywordset', metadata,
    Column('keyword_id', Integer, ForeignKey('keyword.id')),
    Column('photo_id', Integer, ForeignKey('photo.id')),
)


Base = declarative_base()


class Keyword(Base):
    
    __tablename__ = 'keyword'

    id = Column(Integer, primary_key=True)
    word = Column(String)
    level = Column(Integer)
    cont = Column(Integer)
    photos = relationship('Photo', secondary=keywordset_table, backref='keyword')
    
    def __init__(self, word, level):
        self.word = word
        self.level = level


    def getWord(self):
        return self.word

    def setWord(self, word):
        self.word = word
    
    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level
        
    def __repr__(self):
        return "<Keyword('%s','%s')>" % (self.word, self.level)


class Photo(Base):
    
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    info = Column(String)
#    keywords = relationship('Keyword', secondary=keywordset_table, backref='photo')


    def __init__(self, name, address, info):
        self.name = name
        self.address = address
        self.info = info
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address

    def __repr__(self):
        return "<Photo('%s','%s')>" % (self.name, self.address)

metadata.create_all()

Session = sessionmaker(bind=engine)
session = Session()

#key1 = Keyword('interactive',2)
#key2 = Keyword('whiteboard',2)
#key3 = Keyword('wiimote',2)

ep = Photo('Enrique Pelaez', 'enriquepelaez.jpg', 'nn')
kch = Photo('Katherine Chiluiza', 'katherinechiluiza.jpg', 'nn')
sg = Photo('Sixto Garcia', 'sixtogarcia.jpg', 'nn')
xo = Photo('Xavier Ochoa', 'xavierochoa.jpg', 'nn')

session.add(ep)
session.add(kch)
session.add(sg)
session.add(xo)


#session.add_all([
#    Keyword('interactive',2),
#    Keyword('whiteboard',2),
#    Keyword('wiimote',2),
#    Keyword('gesture recognition',2),
#    Keyword('vision',2),
#    Keyword('impaired',2)])

#    Keyword('interactive',2,[kch,xo]),
#    Keyword('whiteboard',2,[kch]),
#    Keyword('wiimote',2,[kch,ep]),
#    Keyword('gesture recognition',2,[kch]),
#    Keyword('vision',2,[xo,sg]),
#    Keyword('impaired',2,[kch,ep])])

session.commit()
