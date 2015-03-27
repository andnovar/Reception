#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

from elixir import *

from model.Keyword import Keyword
from model.Photo import Photo
from model.Person import Person
from model.ResearchArea import ResearchArea
from model.Project import Project
from model.Department import Department
from model.Ubication import Ubication

#metadata.bind = 'mysql://root:andres2012@localhost/recepcion'
metadata.bind = 'sqlite:///recepcion.sqlite'
metadata.bind.echo = True

setup_all(True)

key1 = Keyword(word='interactive', level=3)
key2 = Keyword(word='whiteboard', level=3)
key3 = Keyword(word='wiimote', level=3)
key4 = Keyword(word='gesture recognition', level=3)
key5 = Keyword(word='vision', level=3)
key6 = Keyword(word='impaired', level=3)
key7 = Keyword(word='multitouch', level=3)
key8 = Keyword(word='gobierno', level=3)
key9 = Keyword(word='Sistemas Inteligentes', level=3)
key10 = Keyword(word='educacion', level=3)
key11 = Keyword(word='ministerio', level=3)
key12 = Keyword(word='accesibilidad', level=3)

#CTI

#pers1 = Person(name=u'', last=u'', email='', position=u'')
epelaez = Person(name=u'Enrique', last=u'Pelaez', email='epelaez@cti.espol.edu.ec', position=u'Director del CTI', position_long=u'Director\nCentro de Tecnologías de Información', phone='7030')
mvargas = Person(name=u'María Fernanda', last=u'Vargas', email='mvargas@cti.espol.edu.ec', position=u'Secretaria del CTI', position_long=u'Secretaria\nCentro de Tecnologías de Información', phone='7013')
yandrade = Person(name=u'Yadira', last=u'Andrade', email='yandrade@cti.espol.edu.ec', position=u'Asistente del CTI', position_long=u'Asistente Administrativa\nCentro de Tecnologías de Información', phone='7002')
dchang = Person(name=u'David', last=u'Chang', email='dchang@cti.espol.edu.ec', position=u'Asesor del CTI', position_long=u'Asesor\nCentro de Tecnologías de Información', phone='7022')
parevalo = Person(name=u'Paulina', last=u'Arévalo', email='parevalo@cti.espol.edu.ec', position=u'Web Master y Diseño', position_long=u'Web Master y Diseño Gráfico\nCentro de Tecnologías de Información', phone='7040')

xavier = Person(name=u'Xavier', last=u'Ochoa', email='xavier@cti.espol.edu.ec', position=u'Coordinador TEA', position_long=u'Coordinador Líder de Programa\nTecnología para la Enseñanza y el Aprendizaje\nCentro de Tecnologías de Información', phone='7006')
avinueza = Person(name=u'Alejandro', last=u'Vinueza', email='avinueza@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='775')
fmrivas = Person(name=u'Félix', last=u'Rivas', email='fmrivas@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7040')
icali = Person(name=u'Gustavo', last=u'Cali', email='icali@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7046')
jpincay = Person(name=u'Jhonny', last=u'Pincay', email='jpincay@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='775')
    

sgarcia = Person(name=u'Sixto', last=u'García', email='sgarcia@cti.espol.edu.ec', position=u'Coordinador Líder de Programa', position_long=u'Coordinador Líder de Programa\nTecnología como Asistente Inteligente\nCentro de Tecnologías de Información', phone='7080')
djurado = Person(name=u'David', last=u'Jurado', email='djurado@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7004')
mcheung = Person(name=u'Meiying', last=u'Cheung', email='mcheung@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7036')
caviles = Person(name=u'Carlos', last=u'Avilés', email='caviles@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7004')
csalvatierra = Person(name=u'Carla', last=u'Salvatierra', email='csalvatierra@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7004')
aprieto = Person(name=u'Andrés', last=u'Prieto', email='aprieto@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7004')
ccaceres = Person(name=u'Christopher', last=u'Cáceres', email='ccaceres@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7004')


kchilui = Person(name=u'Katherine', last=u'Chiluiza', email='kchilui@cti.espol.edu.ec', position=u'Coordinadora TCT-DHT', position_long=u'Coordinadora Líder de Programas\nTrabajo, Colaboración y Telepresencia\nDimensiones Humanas de la Tecnología\nCentro de Tecnologías de Información', phone='7031')
portiz = Person(name=u'Pedro', last=u'Ortiz', email='portiz@cti.espol.edu.ec', position=u'Administador del Edificio', position_long=u'Administrador del Edificio PARCON-CTI\nCoordinador de Calidad\nCentro de Tecnologías de Información', phone='7034')
gluzardo = Person(name=u'Gonzalo', last=u'Luzardo', email='gluzardo@cti.espol.edu.ec', position=u'Líder de Proyecto', position_long=u'Líder de Proyecto\nCentro de Tecnologías de Información', phone='7008')
jtibau = Person(name=u'Javier', last=u'Tibau', email='jtibau@cti.espol.edu.ec', position=u'Líder de Proyecto', position_long=u'Líder de Proyecto\nCentro de Tecnologías de Información', phone='7037')
vecheverria = Person(name=u'Vanessa', last=u'Echeverría', email='vecheverria@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7044')
avargas = Person(name=u'Andrés', last=u'Vargas', email='avargas@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7037')
bguaman = Person(name=u'Bruno', last=u'Guamán', email='bguaman@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7037')
efrainastudillo = Person(name=u'Efraín', last=u'Astudillo', email='efrain.astudillo@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='7037')
mmora = Person(name=u'Mónica', last=u'Mora', email='mmora@cti.espol.edu.ec', position=u'Asistente de Investigación', position_long=u'Asistente de Investigación\nCentro de Tecnologías de Información', phone='8014')


gjimenez = Person(name=u'Gerald', last=u'Jiménez', email='gjimenez@cti.espol.edu.ec', position=u'Administrador del Área Tecnológica', position_long=u'Administrador del Área Tecnológica\nCentro de Tecnologías de Información', phone='7032')
mcoronel = Person(name=u'Mario', last=u'Coronel', email='mcoronel@cti.espol.edu.ec', position=u'Asistente Técnico', position_long=u'Administrador de Redes y Servidores\nCentro de Tecnologías de Información', phone='778')
jgalarza = Person(name=u'Jorge', last=u'Galarza', email='jgalarza@cti.espol.edu.ec', position=u'Asistente Técnico', position_long=u'Asistente Técnico\nCentro de Tecnologías de Información', phone='778')
jmunoz = Person(name=u'José', last=u'Muñoz', email='jmunoz@cti.espol.edu.ec', position=u'Asistente Técnico', position_long=u'Asistente Técnico\nCentro de Tecnologías de Información', phone='778')

#CICYT

jcaldero = Person(name=u'Jorge', last=u'Calderón', email='jcaldero@espol.edu.ec', position=u'Decano de la Facultad de Posgrado', position_long=u'Decano de la Facultad de Posgrado\nDirector del CICYT', phone='761')
aherrera = Person(name=u'Paúl', last=u'Herrera', email='aherrera@espol.edu.ec', position=u'Subdecano de la Facultad de Posgrado', position_long=u'Subdecano de la Facultad de Posgrado', phone='742')
csegarra = Person(name=u'Clara', last=u'Segarra', email='csegarra@espol.edu.ec', position=u'Asitente Técnico Académico', position_long=u'Asitente Técnico Académico', phone='762')
svera    = Person(name=u'Catalina', last=u'Vera Moscoso', email='svera@espol.edu.ec', position=u'Asistente Finaciera', position_long=u'Asistente Finaciera', phone='763')
eaguilar = Person(name=u'Edmundo', last=u'Aguilar', email='eaguilar@espol.edu.ec', position=u'Asistente Técnico Administrativo', position_long=u'Asistente Técnico Administrativo', phone='764')
jponcec  = Person(name=u'Johanna', last=u'Ponce', email='jponcec@espol.edu.ec', position=u'Secretaria del CICYT', position_long=u'Secretaria del CICYT\n Coordinador de Calidad del CICYT', phone='760')
clespin  = Person(name=u'César', last=u'Espín', email='clespin@espol.edu.ec', position=u'Auxiliar Administrativo Financiero', position_long=u'Auxiliar Administrativo Financiero', phone='763')
galameri = Person(name=u'Galo', last=u'Merino', email='galameri@espol.edu.ec', position=u'Ayudante', position_long=u'Ayudante', phone='760')
stacle   = Person(name=u'Sami', last=u'Tacle', email='stacle@espol.edu.ec', position=u'Coordinadora de Innovación del CICYT', position_long=u'Coordinadora de Innovación del CICYT', phone='769')

 
#p5 = Photo(name=u'', address='', keywords=[])
photo_epelaez = Photo(name=u'', address='epelaez.jpg', keywords=[], person=epelaez)
photo_mvargas = Photo(name=u'', address='mvargas.jpg', keywords=[], person=mvargas)
photo_yandrade = Photo(name=u'', address='yandrade.jpg', keywords=[], person=yandrade)
photo_dchang = Photo(name=u'', address='dchang.jpg', keywords=[], person=dchang)
photo_parevalo = Photo(name=u'', address='parevalo.jpg', keywords=[], person=parevalo)

photo_xavier = Photo(name=u'', address='xavier.jpg', keywords=[], person=xavier)
photo_avinueza = Photo(name=u'', address='avinueza.jpg', keywords=[], person=avinueza)
photo_fmrivas = Photo(name=u'', address='fmrivas.jpg', keywords=[], person=fmrivas)
photo_icali = Photo(name=u'', address='icali.jpg', keywords=[], person=icali)
photo_jpincay = Photo(name=u'', address='jpincay.jpg', keywords=[], person=jpincay)

photo_sgarcia = Photo(name=u'', address='sgarcia.jpg', keywords=[], person=sgarcia)
photo_djurado = Photo(name=u'', address='djurado.jpg', keywords=[], person=djurado)
photo_mcheung = Photo(name=u'', address='mcheung.jpg', keywords=[], person=mcheung)
photo_caviles = Photo(name=u'', address='caviles.jpg', keywords=[], person=caviles)
photo_csalvatierra = Photo(name=u'', address='csalvatierra.jpg', keywords=[], person=csalvatierra)
photo_aprieto = Photo(name=u'', address='aprieto.jpg', keywords=[], person=aprieto)
photo_ccaceres = Photo(name=u'', address='ccaceres.jpg', keywords=[], person=ccaceres)

photo_kchilui = Photo(name=u'', address='kchilui.jpg', keywords=[], person=kchilui)
photo_portiz = Photo(name=u'', address='portiz.jpg', keywords=[], person=portiz)
photo_gluzardo = Photo(name=u'', address='gluzardo.jpg', keywords=[], person=gluzardo)
photo_jtibau = Photo(name=u'', address='jtibau.jpg', keywords=[], person=jtibau)
photo_vecheverria = Photo(name=u'', address='vecheverria.jpg', keywords=[], person=vecheverria)
photo_avargas = Photo(name=u'', address='avargas.jpg', keywords=[], person=avargas)
photo_bguaman = Photo(name=u'', address='bguaman.jpg', keywords=[], person=bguaman)
photo_efrainastudillo = Photo(name=u'', address='efrain.astudillo.jpg', keywords=[], person=efrainastudillo)
photo_mmora = Photo(name=u'', address='mmora.jpg', keywords=[], person=mmora)

photo_gjimenez = Photo(name=u'', address='gjimenez.jpg', keywords=[], person=gjimenez)
photo_mcoronel = Photo(name=u'', address='mcoronel.jpg', keywords=[], person=mcoronel)
photo_jgalarza = Photo(name=u'', address='jgalarza.jpg', keywords=[], person=jgalarza)
photo_jmunoz   = Photo(name=u'', address='jmunoz.jpg', keywords=[], person=jmunoz)

#CICYT
photo_jcaldero = Photo(name='', address='jcaldero.jpg', keywords=[], person=jcaldero)
photo_aherrera = Photo(name='', address='aherrera.jpg', keywords=[], person=aherrera)
photo_csegarra = Photo(name='', address='csegarra.jpg', keywords=[], person=csegarra)
photo_svera    = Photo(name='', address='svera.jpg'   , keywords=[], person=svera)
photo_eaguilar = Photo(name='', address='eaguilar.jpg', keywords=[], person=eaguilar)
photo_jponcec  = Photo(name='', address='jponcec.jpg' , keywords=[], person=jponcec)
photo_clespin  = Photo(name='', address='clespin.jpg' , keywords=[], person=clespin)
photo_galameri = Photo(name='', address='galameri.jpg', keywords=[], person=galameri)
photo_stacle   = Photo(name='', address='stacle.jpg'  , keywords=[], person=stacle)

#ra1 = ResearchArea(name=u'', description=u'', alias='', persons=[])
tct = ResearchArea(name=u'Trabajo, Colaboración y Telepresencia', description=u'', alias='TCT', persons=[portiz, gluzardo, jtibau, vecheverria, avargas, bguaman, efrainastudillo, mmora])
tai = ResearchArea(name=u'Tecnología como Asistente Inteligente', description=u'', alias='TAI', persons=[djurado, mcheung, caviles, csalvatierra, aprieto, ccaceres])
tea = ResearchArea(name=u'Tecnología para la Enseñanza y el Aprendizaje', description=u'', alias='TEA', persons=[avinueza, fmrivas, icali, jpincay])
cicyt = ResearchArea(name=u'Centro de Investigación, Científica y Tecnológica', description=u'', persons=[jcaldero, aherrera, csegarra, svera, eaguilar, jponcec, clespin, galameri, stacle])

#proj1 = Project(name=u'', description=u'', doc='', persons=[], keywords=[])
proj1 = Project(name=u'Sistema Multimedia Interactivo de Busqueda de Info', description=u'Busqueda de informacion por medio de una pantalla multitouch de bajo costo, principalmente la busqueda se la realiza por palabras de interes.', doc='multitouch.pdf', persons=[avargas], keywords=[key1, key7])
proj3 = Project(name=u'SIGLIT Ministerio del Litoral', description=u'Poner a disposicion de las entidades gubernamentales, desde ministerios, secretarias, sub-secretarias, municipios, juntas parroquiales, asi como de organizaciones sociales de 6 provincias un sistema de informacion que permita orientar la toma de decisiones para la planificacion /gestion del desarrollo regional y local y la formulacion /ejecucion de iniciativas orientadas al desarrollo local, manejo sustentable de los recursos naturales, el fortalecimiento organizativo y el logro del bienestar economico.', doc='siglit.pdf', persons=[sgarcia], keywords=[key10, key11])
proj4 = Project(name=u'Sistema de Administración de Contenidos Web de Codigo abierto para la inclusion de personas con Discapacidades Visuales, a partir de una metodologia de Evaluacion Integral', description=u'Este proyecto busca desarrollar una metodologia de evaluacion de sitios web que garanticen accesibilidad, en especial, para usuarios no videntes. ', doc='accesibilidad.pdf', persons=[kchilui], keywords=[key12, key6])
proj5 = Project(name=u'Hand Gesture Recognition Interface', description=u'Probar la eficiencia de las metodologias empleadas actualmente en la ensenanza de la audicion deteriorada de los ninos mediante la incorporacion de nuevas tecnologias.', doc='eminds.pdf', persons=[kchilui], keywords=[key4,key6])

#dep1 = Department(alias='', name=u'', description=u'', persons=[])
dep1 = Department(alias='FIEC', name=u'Facultad de Ingenieria en Electricidad y Computacion', description=u'Ofrece carreras de Ingenieria principalmente las que tienen que ver con el desarrollo de Tecnologías nuevas.', persons=[avargas])
dep2 = Department(alias='FIMCP', name=u'Facultad de Ingenieria en Mecanica y Ciencias de la Produccion')

#ubi1 = Ubication(name=u'Centro Tecnologia de Informacion (CTI)', x=1105, y=855, persons=[pers1, pers2, pers3, pers4, pers5, pers6, pers7, pers8, pers9])
cti_building = Ubication(building='PARCON', name=u'Centro de Tecnologías de Información', x=1105, y=855, persons=[kchilui, epelaez, mvargas, yandrade, dchang, parevalo, xavier, jgalarza, mcoronel, jmunoz, gjimenez, sgarcia, portiz, gluzardo, jtibau, vecheverria, avargas, bguaman, efrainastudillo, mmora, djurado, mcheung, caviles, csalvatierra, aprieto, ccaceres, avinueza, fmrivas, icali, jpincay ])
cicyt_building = Ubication(building='PARCON', name=u'Centro de Investigación en Ciencia y Tecnología', x=1105, y=855, persons=[jcaldero, aherrera, csegarra, svera, eaguilar, jponcec, clespin, galameri, stacle])

session.commit()

print Keyword.query.all()
print Project.query.all()
photo = Photo.query.filter_by(address='avargas.jpg').one()
p = photo.getPerson()
ra = p.getResearchArea()
projs = p.getProjects()

#print photo.getPerson()
