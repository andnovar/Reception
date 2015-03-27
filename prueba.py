#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

#from Conector import Conector
#from Mensaje import Mensaje
#from Llamada import LlamadaEntrante, LlamadaSaliente, Llamada
#
#parameters = {'account':  '7045@pbx.cti.espol.edu.ec',
#              'password': 'avargas'
#             }

#parameters = {'account':  'recepcion@cti.espol.edu.ec',
#              'password': 'recepcioncti2011',
#              'server' : 'talk.google.com',
#              'port': 5222,
#              'ignore-ssl-errors': True
#              }
#
#incon = Conector('sofiasip','sip', parameters)
#
#incon = Conector('gabble','jabber', parameters)
#
#con = Mensaje(conn,'Este es un mensaje de prueba', 'avargas@cti.espol.edu.ec', 5000, None)
#con.run()

#call = LlamadaEntrante(incon)
#
#call = LlamadaSaliente(incon, '7037@pbx.cti.espol.edu.ec')
#call = LlamadaSaliente(incon, 'avargas@cti.espol.edu.ec')
#call.run()
#from elixir import *
#
#from model.Photo import Photo
#from model.Person import Person
#from model.ResearchArea import ResearchArea
#from model.Ubication import Ubication
#from model.Department import Department
#from model.Keyword import Keyword
#from model.Project import Project
#
#metadata.bind = 'sqlite:///recepcion.sqlite'
##metadata.bind.echo = True
#setup_all(True)
#
#p = Person.query.filter_by(id=1).one()
#
#print p
#print p.getEmail()

from Call import Call

a = Call('7045', 'avargas')
a.make_call('7037')