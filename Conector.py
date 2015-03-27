from telepathy.interfaces import (CONN_MGR_INTERFACE, CONN_INTERFACE)
from telepathy.client.managerregistry import ManagerRegistry
from telepathy.client.conn import Connection


class Conector:
    
    def __init__(self, manager, protocol, parameters):
        self.manager = manager
        self.protocol = protocol
        self.parameters = parameters
    
    def establecer_conexion(self, ready_handler=None):
        reg = ManagerRegistry()
        reg.LoadManagers()
        mgr = reg.GetManager(self.manager)
        bus_name, object_path = mgr[CONN_MGR_INTERFACE].RequestConnection(self.protocol, self.parameters)
        conn = Connection(bus_name, object_path, ready_handler=None)
        print "connecting"
        conn[CONN_INTERFACE].Connect()
        print "connected"
        return conn

    def establecer_conexion_llamada(self, ready_handler=None):
        reg = ManagerRegistry()
        reg.LoadManagers()
        mgr = reg.GetManager(self.manager)
        bus_name, object_path = mgr[CONN_MGR_INTERFACE].RequestConnection(self.protocol, self.parameters)
        conn = Connection(bus_name, object_path, ready_handler=ready_handler)
        return conn