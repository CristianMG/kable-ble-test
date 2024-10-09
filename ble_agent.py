import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib

AGENT_INTERFACE = "org.bluez.Agent1"
AGENT_PATH = "/test/agent"
AGENT_MANAGER = "org.bluez.AgentManager1"
CAPABILITY = "DisplayOnly"

class Agent(dbus.service.Object):
    def __init__(self, bus, path):
        super().__init__(bus, path)

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Release(self):
        print("Agent liberado")

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        print(f"RequestPinCode llamado para {device}")
        return "1234"

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="u")
    def RequestPasskey(self, device):
        print(f"RequestPasskey llamado para {device}")
        return dbus.UInt32(1234)

    @dbus.service.method(AGENT_INTERFACE, in_signature="ouq", out_signature="")
    def DisplayPasskey(self, device, passkey, entered):
        print(f"DisplayPasskey llamado para {device}, Passkey: {passkey}, Ingresado: {entered}")

    @dbus.service.method(AGENT_INTERFACE, in_signature="os", out_signature="")
    def DisplayPinCode(self, device, pincode):
        print(f"DisplayPinCode llamado para {device}, PIN: {pincode}")

    @dbus.service.method(AGENT_INTERFACE, in_signature="ou", out_signature="")
    def RequestConfirmation(self, device, passkey):
        print(f"RequestConfirmation llamado para {device}, Passkey: {passkey}")
        return

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="")
    def RequestAuthorization(self, device):
        print(f"RequestAuthorization llamado para {device}")
        return

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Cancel(self):
        print("Emparejamiento cancelado")

def register_agent(bus):
    manager = dbus.Interface(
        bus.get_object("org.bluez", "/org/bluez"),
        AGENT_MANAGER
    )
    
    agent = Agent(bus, AGENT_PATH)
    
    manager.RegisterAgent(AGENT_PATH, CAPABILITY)
    print("Agente registrado")
    
    manager.RequestDefaultAgent(AGENT_PATH)
    print("Agente establecido como predeterminado")

    return agent

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    agent = register_agent(bus)
    mainloop = GLib.MainLoop()
    
    print("Agente Bluetooth ejecutándose. Presiona Ctrl+C para salir.")
    
    try:
        mainloop.run()
    except KeyboardInterrupt:
        print("Agente Bluetooth detenido.")