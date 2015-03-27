import sys
import pjsua as pj

LOG_LEVEL=3
current_call = None

# Callback to receive events from account
class MyAccountCallback(pj.AccountCallback):

    def __init__(self, account=None):
        pj.AccountCallback.__init__(self, account)

    # Notification on incoming call
    def on_incoming_call(self, call):
        global current_call 
        if current_call:
            call.answer(486, "Busy")
            return
            
        print "Incoming call from ", call.info().remote_uri
        print "Press 'a' to answer"

        current_call = call

        call_cb = MyCallCallback(current_call)
        current_call.set_callback(call_cb)

        current_call.answer(180)

        
# Callback to receive events from Call
class MyCallCallback(pj.CallCallback):

    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)

    # Notification when call state has changed
    def on_state(self):
        global current_call
        print "Call with", self.call.info().remote_uri,
        print "is", self.call.info().state_text,
        print "last code =", self.call.info().last_code, 
        print "(" + self.call.info().last_reason + ")"

        
        if self.call.info().state == pj.CallState.DISCONNECTED:
            current_call = None
            print 'Current call is', current_call

    # Notification when call's media state has changed.
    def on_media_state(self):
        global player
        if self.call.info().media_state == pj.MediaState.ACTIVE:
            # Disconnect the ring ring
            pj.Lib.instance().conf_disconnect(1, 0)
            # Connect the call to sound device
            call_slot = self.call.info().conf_slot
            pj.Lib.instance().conf_connect(call_slot, 0)
            pj.Lib.instance().conf_connect(0, call_slot)
            print "Media is now active"
        else:
            print "Media is inactive"


class Call:
    
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.colgar = False
            
    # Function to make call
    def make_call(self, ext):
        global current_call
        global player
        lib = pj.Lib()
        try:
            # Init library with default config and some customized
            # logging config.
            lib.init(log_cfg = pj.LogConfig(level=LOG_LEVEL, callback=self.log_cb))
        
            # Create UDP transport which listens to any available port
            transport = lib.create_transport(pj.TransportType.UDP, 
                                             pj.TransportConfig(0))
            print "\nListening on", transport.info().host, 
            print "port", transport.info().port, "\n"
            #lib.set_snd_dev(1, 1)
            # Start the library
            lib.start()
        
            # Create local account
            acc_cfg = pj.AccountConfig("pbx.cti.espol.edu.ec", self.user, self.password)

            acc_cb = MyAccountCallback()
            acc = lib.create_account(acc_cfg, cb=acc_cb)
        
            # If argument is specified then make call to the URI
            lck = lib.auto_lock()
            print "Making call to sip:"+ext+"@pbx.cti.espol.edu.ec"
            current_call = acc.make_call("sip:"+ext+"@pbx.cti.espol.edu.ec", cb=MyCallCallback())
            print 'Current call is', current_call
            del lck
            
            player = lib.create_player("CallRingingOut.wav", True)
            lib.conf_connect(lib.player_get_slot(player), 0)
            
            my_sip_uri = "sip:" + transport.info().host + \
                         ":" + str(transport.info().port)
        
            # Menu loop
            while True:
#                print "My SIP URI is", my_sip_uri
#                print "Menu:  m=make call, h=hangup call, a=answer call, q=quit"

                if not current_call:
                    break
                
                if self.colgar:
                    self.colgar = False
                    current_call.hangup()
                    
#                entrada = sys.stdin.readline().rstrip("\r\n")
#                if entrada == "m":
#                    if current_call:
#                        print "Already have another call"
#                        continue
#                    print "Enter destination URI to call: ", 
#                    entrada = sys.stdin.readline().rstrip("\r\n")
#                    if entrada == "":
#                        continue
#                    lck = lib.auto_lock()
#                    current_call = self.make_call(entrada)
#                    del lck
#        
#                elif entrada == "h":
#                    if not current_call:
#                        print "There is no call"
#                        continue
#                    current_call.hangup()
#        
#                elif entrada == "a":
#                    if not current_call:
#                        print "There is no call"
#                        continue
#                    current_call.answer(200)
#        
#                elif entrada == "q":
#                    break
        
            # Shutdown the library
            transport = None
            acc.delete()
            acc = None
            lib.destroy()
            lib = None
        except pj.Error, e:
            print "Exception: " + str(e)
            lib.destroy()
            lib = None
            return '0'
        return '1'
    
    def hangup(self):
        if not current_call:
            print "There is no call"
        self.colgar = True
    
    def log_cb(self, level, str, len):
        print str,
