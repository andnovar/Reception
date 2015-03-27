#!/usr/bin/python
# -*- coding: latin-1 -*-

import kivy
import time

from threading import Thread

kivy.require('1.0.9')

#Load communication classes with telepathy
from Conector import Conector
from Mensaje import Mensaje
#Load communication classes with PJSUA
from Call import Call

#Load graphical widgets
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

#Load Kivy Core
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock

#Load Persistence Engine
from elixir import *

#Load the model we are going to use
from model.Photo import Photo
from model.Person import Person
from model.ResearchArea import ResearchArea
from model.Ubication import Ubication
from model.Department import Department
from model.Keyword import Keyword
from model.Project import Project

#Telepathy constants and interfaces
from telepathy.interfaces import (CONN_INTERFACE, CONNECTION_INTERFACE_REQUESTS, CHANNEL, CHANNEL_TYPE_CONTACT_LIST)
from telepathy.constants import HANDLE_TYPE_GROUP

#Handles to use Threads into the main Kivy Thread
from kivy.support import install_gobject_iteration
install_gobject_iteration()

#Initial Parameters Persistence Engine, Gtalk Account and SIP Account
metadata.bind = 'sqlite:///recepcion.sqlite'
setup_all(True)
parameters = {'account':  'recepcion@cti.espol.edu.ec',
              'password': 'recepcioncti2011',
              'server' : 'talk.google.com',
              'port': 5222,
              'ignore-ssl-errors': True
              }
incon = Conector('gabble','jabber', parameters)
conn = incon.establecer_conexion()
parent = Widget()

class Sisrecmatico(FloatLayout):
    def do_cti(self):
        global parent
        parent.clear_widgets()
        c = Integrantesui_cti(size=(1024, 768))
        parent.add_widget(c)
        
    def do_cicyt(self):
        global parent
        parent.clear_widgets()
        c = Integrantesui_cicyt(size=(1024, 768))
        parent.add_widget(c)

class Integrantesui_cti(FloatLayout):
    
    p = Person()
    
    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)

    def do_return(self):
        global parent
        parent.clear_widgets()
        a = Sisrecmatico(size=(1024, 768))
        parent.add_widget(a)

    def do_begin(self):
        global parent
        parent.clear_widgets()
        a = Sisrecmatico(size=(1024, 768))
        parent.add_widget(a)
    
    def information(self):
        popup = MyPopupWithBackground(title='Información',
        content=Label(text='Si desea información por favor escribale a María Fernanda Vargas'),
        size_hint=(None, None), size=(400, 400), auto_dismiss=True)
        popup.open()
        
    def do_info(self, iden):
        self.p = Person.query.filter_by(id=iden).one()
        popup = Popup(title='' + self.p.getFullName(), size_hint=(None, None),separator_color=(1,1,1,1), size=(716, 560),background_color=(0,0,0,0.5),background=('images/layout/fondoPopup.png'))     
        b = Info(self.p, popup)
        b.dibujar(self.p.getPhotos()[0])
        popup.content = b
        popup.bind(on_dismiss=b.resetearmensajerec)
        popup.open()

class Info(FloatLayout):
    
    respuesta = StringProperty('')
    colgado = StringProperty('0')
    a = Call('7045', 'avargas')
    llamando = False
    
    def __init__(self, p, popup, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        self.bind(respuesta=self.my_callback)
        self.bind(colgado=self.closedcall_callback)
        self.p = p

    def dibujar(self,foto):
        lay = BoxLayout(orientation='vertical', size=(716,400), x=150, y=160)
        self.add_widget(lay)
        
        #First Row - Field for the name and button Send
        
        self.boxtit = BoxLayout(orientation='horizontal', padding=20, spacing=10, size_hint = (1, 0.3))
        self.mensaje = TextInput(text='Si desea enviar un mensaje escriba su nombre aquí', font_size=15)
        self.mensaje.bind(focus = self.set_null_message)
        btn_enviar_msg = Button(text='', font_size=15, size_hint=(None, None), size=(120,65),background_normal=("images/layout/enviar.png"),background_down=("images/layout/enviarDown.png") )
        btn_enviar_msg.bind(on_release = self.initThreadMsg)
        self.boxtit.add_widget(self.mensaje)
        self.boxtit.add_widget(btn_enviar_msg)
        
        
        #Second Row - Image and Person's information
        box = BoxLayout(orientation='horizontal', size_hint = (1,0.6), padding=10 )
        self.box2 = BoxLayout(orientation='horizontal')
        
        self.btn_llamar = Button(text='', font_size=15, size_hint=(None, None), size=(140,80), background_normal=("images/layout/teleL.png"),background_down=("images/layout/teleLDown.png"))
        self.btn_llamar.bind(on_release = self.initThreadCall)
        #Labels to position Call button and Hang up button centered
        l1 = Label(text='', font_size=18,size_hint=(0.5,1))
        l2 = Label(text='', font_size=18,size_hint=(0.5,1))
        self.box2.add_widget(l1)
        self.box2.add_widget(self.btn_llamar)
        self.box2.add_widget(l2)
        
        img = Image(source='images/people/' + foto.getAddress(), size_hint = (0.3,1))
        boxint = BoxLayout(orientation='vertical', size_hint=(0.8, 1))
        labelnom = Label(text=self.p.getFullName()+'\n'+self.p.getPosition()+'\n'+self.p.getUbication().getName(), font_size=18)
        boxint.add_widget(labelnom)
        boxint.add_widget(self.box2)
        
        box.add_widget(img)
        box.add_widget(boxint)
        
        #Third Row - Call button and Hang up button
        
        
        self.l3 = Label(text='Llamando... Espere por favor', font_size=18,size_hint=(0.5,1))
        self.btn_colgar = Button(text='', font_size=15,size_hint=(None, None), size=(140,80),background_normal=("images/layout/teleC.png"),background_down=("images/layout/teleCDown.png"))
        self.btn_colgar.bind(on_release=self.prepareCall)
        self.box3 = BoxLayout(orientation='horizontal',padding=20, spacing=10, size_hint = (1, 0.1))
        
        # Adding everything to the main container
        lay.add_widget(box)
        lay.add_widget(self.box3)
        lay.add_widget(self.boxtit)
        
    def set_null_message(self, instance, value):
        self.mensaje.text = ''
        
    def do_message(self, msg, dest, time):
        global conn
        self.msg = Mensaje(conn, msg, dest, time, self.recvd_cb)
        self.msg.run()
    
    def initThreadMsg(self, instance):
        try:
            if self.mensaje.text != "" and self.mensaje.text != 'Si desea enviar un mensaje escriba su nombre aquí':
#                t2 = Thread(target=self.do_message, args=(self.mensaje.text + ' lo está buscando en Recepción, por favor comuníquese', self.p.getEmail(), 5000))
                t2 = Thread(target=self.do_message, args=(self.mensaje.text + ' Este es un mensaje de prueba no hacer caso', self.p.getEmail(), 5000))
                t2.start()
        except Exception, e:
            print str(e)
    
    def recvd_cb(self, *args):
        id, timestamp, sender, type, flags, text = args
        self.respuesta = text
        self.msg.quit()
    
    def do_mostrar_resp(self, dt):
        if self.respuesta == '':
            pass
        else:
            frespuesta = TextInput()
            contenedor = BoxLayout(orientation='vertical')
            frespuesta.text = self.respuesta
            acept = Button(text='Aceptar')
            contenedor.add_widget(frespuesta)
            contenedor.add_widget(acept)
            popuprecibe = Popup(title='Mensaje Recibido ...', content=contenedor, size_hint=(None, None), size=(400,400), auto_dismiss=False)
            acept.bind(on_release=popuprecibe.dismiss)
            popuprecibe.bind(on_dismiss=self.resetearmensajerec)
            popuprecibe.open()

    def resetearmensajerec(self, instance):
        self.respuesta = ''
        if self.llamando:
            self.a.hangup()

    def initThreadCall(self, instance):
        self.llamando = True
        try:
            t = Thread(target=self.do_call)
            t.start()
            self.box3.add_widget(self.l3)
            self.box2.clear_widgets()
            l1 = Label(text='', font_size=18,size_hint=(0.5,1))
            l2 = Label(text='', font_size=18,size_hint=(0.5,1))
            self.box2.add_widget(l1)
            self.box2.add_widget(self.btn_colgar)
            self.box2.add_widget(l2)
        except Exception, e:
            print str(e)
    
    def prepareCall(self, instance):
        
        self.llamando = False
        try:
            self.a.hangup()
            self.box3.remove_widget(self.l3)
            self.box2.clear_widgets()
            wimg = Image(source='loading.gif')
            self.box2.add_widget(wimg)
        except Exception,e:
            print str(e)
    
    def do_call(self):
        self.colgado = self.a.make_call(str(self.p.getPhone()))
    
    def my_callback(self, instance, value):
        Clock.schedule_once(self.do_mostrar_resp)
    
    def closedcall_callback(self, instance, value):
        Clock.schedule_once(self.draw_closedcall)
    
    def draw_closedcall(self, dt):
        self.llamando = False
        if self.colgado == '1':
            self.box3.remove_widget(self.l3)
            self.box2.clear_widgets()
            l1 = Label(text='', font_size=18,size_hint=(0.5,1))
            l2 = Label(text='', font_size=18,size_hint=(0.5,1))
            self.box2.add_widget(l1)
            self.box2.add_widget(self.btn_llamar)
            self.box2.add_widget(l2)
            self.colgado = '0'

    def do_back(self, instance):
        global parent
        parent.clear_widgets()
        c = Integrantesui_cti(size=(1024, 768))
        parent.add_widget(c)


class Integrantesui_cicyt(FloatLayout):
    
    respuesta = StringProperty('')
    p = Person()
    
    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)

    def do_return(self):
        global parent
        parent.clear_widgets()
        a = Sisrecmatico(size=(1024, 768))
        parent.add_widget(a)

    def do_begin(self):
        global parent
        parent.clear_widgets()
        a = Sisrecmatico(size=(1024, 768))
        parent.add_widget(a)

    def information(self):
        popup = MyPopupWithBackground(title='Información',
        content=Label(text='Llame a alguna persona del CICYT'),
        size_hint=(None, None), size=(400, 400), auto_dismiss=True)
        popup.open()
        
    def do_info(self, iden):
        self.p = Person.query.filter_by(id=iden).one()
        popup = Popup(title='' + self.p.getFullName(),separator_color=(1,1,1,1), size_hint=(None, None), size=(716, 560),background_color=(0,0,0,0.5),background=('images/layout/fondoPopup.png'))     
        b = Info(self.p, popup)
        b.dibujar(self.p.getPhotos()[0])
        popup.content = b
        popup.bind(on_dismiss=b.resetearmensajerec)
        popup.open()

    def do_mostrar_resp(self, dt):
        if self.respuesta == '':
            pass
        else:
            frespuesta = TextInput()
            contenedor = BoxLayout(orientation='vertical')
            frespuesta.text = self.respuesta
            acept = Button(text='Aceptar')
            contenedor.add_widget(frespuesta)
            contenedor.add_widget(acept)
            popuprecibe = Popup(title='Mensaje Recibido ...', content=contenedor, size_hint=(None, None), size=(400,400), auto_dismiss=False)
            acept.bind(on_release=popuprecibe.dismiss)
            popuprecibe.open()
        
    def do_message(self, msg, dest, time):
        global conn
        msg = Mensaje(conn, msg, dest, time, self.recvd_cb)
        msg.run()

    def recvd_cb(self, *args):
        id, timestamp, sender, type, flags, text = args
        self.respuesta = text

    def  passmy_callback(self, instance, value):
        Clock.schedule_once(self.do_mostrar_resp)
 
    def resetearmensajerec(self, instance):
        self.respuesta = ''


class MyLabelWithBackground(Label):
    pass

class MyPopupWithBackground(Popup):
    pass

class SisrecmaticoApp(App):
    def build(self):
        global parent
        a = Sisrecmatico(size=(1024, 768))
        parent.add_widget(a)
        return parent
    
    def on_stop(self):
        global conn
        try:
            conn[CONN_INTERFACE].Disconnect()
        except Exception, e:
            print e

if __name__ in ('__android__', '__main__'):
    SisrecmaticoApp().run()
