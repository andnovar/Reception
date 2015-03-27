import dbus.glib
import gobject

from telepathy.constants import (CONNECTION_HANDLE_TYPE_CONTACT, CONNECTION_STATUS_CONNECTED, CHANNEL_TEXT_MESSAGE_TYPE_NORMAL)
from telepathy.client.channel import Channel
from telepathy.interfaces import (CHANNEL_TYPE_TEXT, CONN_INTERFACE, CHANNEL_INTERFACE)

# install the gobject iteration
#from kivy.support import install_gobject_iteration
#install_gobject_iteration()


class Mensaje:
    
    def __init__(self, conexion, mensaje, destinatario, time, respuesta):
        self.recvd_cb = respuesta
        self.mensaje = mensaje
        self.dest = destinatario
        self.conn = conexion
        self.conn.call_when_ready(self.ready_cb)
        self.time = time
    
    def ready_cb(self, conn):
        print "connected"
        # Getting the identifier for a contact
        # A Handle could represent a contact or a chat room, contact list, etc.
        handle = self.conn[CONN_INTERFACE].RequestHandles(CONNECTION_HANDLE_TYPE_CONTACT, [self.dest])[0]
        print 'got handle %d for %s' % (handle, self.dest)
        
        
        self.channel = self.conn.request_channel(CHANNEL_TYPE_TEXT, CONNECTION_HANDLE_TYPE_CONTACT, handle, True)
        
        print 'got text channel with handle (%d,%d)' % (CONNECTION_HANDLE_TYPE_CONTACT, handle)
        
        self.channel[CHANNEL_TYPE_TEXT].connect_to_signal('Sent', self.sent_cb)
        self.channel[CHANNEL_TYPE_TEXT].connect_to_signal('Received', self.recvd_cb)
        self.channel[CHANNEL_TYPE_TEXT].connect_to_signal('SendError', self.send_error_cb)
        
        if self.mensaje is not None:
            self.channel[CHANNEL_TYPE_TEXT].Send(CHANNEL_TEXT_MESSAGE_TYPE_NORMAL, self.mensaje)
        else:
            for msg in self.channel[CHANNEL_TYPE_TEXT].ListPendingMessages(True):
                self.recvd_cb(*msg)
                
    

    def sent_cb(self, timestamp, type, text):
        print 'message sent: """%s"""' % text
        # if we Disconnect() immediately, the message might not actually
        # make it to the network before the socket is shut down (this can
        # be the case in Gabble) - as a workaround, delay before disconnecting
        gobject.timeout_add(self.time, self.quit)

    def send_error_cb(self, error, timestamp, type, text):
        print 'error sending message: code %d' % error
        self.quit()
        
    def run(self):
        print "main loop running"
        self.loop = gobject.MainLoop()

        try:
            self.loop.run()
        finally:
            print "!!!!!!!!!!!En el finally!!!!!!!!!!!"
#            self.channel[CHANNEL_INTERFACE].Close()
#            self.conn[CONN_INTERFACE].Disconnect()

    def quit(self):
        if self.loop:
            print 'Cerrando Canal !!!!!'
            self.channel[CHANNEL_INTERFACE].Close()
            self.loop.quit()
            self.loop = None
                
#Este bloque pide un canal para iniciar la conversacion ################################
    def status_changed_cb(self, state, reason):
        if state != CONNECTION_STATUS_CONNECTED:
            return
        # Getting the identifier for a contact
        # A Handle could represent a contact or a chat room, contact list, etc.
        handle = self.conn[CONN_INTERFACE].RequestHandles(CONNECTION_HANDLE_TYPE_CONTACT, [self.dest])[0]
        # Creating the channel used for communication
        # it could be Text, VOIP/video, contact list
        self.conn[CONN_INTERFACE].RequestChannel(CHANNEL_TYPE_TEXT, CONNECTION_HANDLE_TYPE_CONTACT, handle, True)

    def new_channel_cb(self, object_path, channel_type, handle_type, handle, suppress_handler):
        if channel_type != CHANNEL_TYPE_TEXT:
            return
        channel = Channel(self.conn.service_name, object_path)
        channel[CHANNEL_TYPE_TEXT].Send(CHANNEL_TEXT_MESSAGE_TYPE_NORMAL, self.mensaje)
    
    def EnviarMensaje(self):
        # Waiting for a status changed
        self.conn[CONN_INTERFACE].connect_to_signal('StatusChanged', self.status_changed_cb)
        # Waiting for a new channel
        self.conn[CONN_INTERFACE].connect_to_signal('NewChannel', self.new_channel_cb)

##########################################################################################

    def setMensaje(self, newmsg):
        self.mensaje = newmsg
    
    
