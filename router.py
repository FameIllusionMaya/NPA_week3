"""NPA week3 homework define python class as router"""

class Router:
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.router_interface = {}

    def add_interface(self, interface):
        """add only interface to router"""
        self.router_interface[interface] = "unassign"
        print("add interface %s Done!" %(interface))

    def add_interface_ip(self, interface, ip):
        """assign ip to an interface or add interface and ip"""
        self.router_interface[interface] = ip
        print(self.router_interface)

    def connect_to(self):
        """connect device with another in topology graph"""

    # def show_interface(self):
    # def show_neighbor(self):

r1 = Router('Cisco', 'IOSv', 'R1')
r2 = Router('Cisco', '3745', 'R2')
r3 = Router('Juniper', 'MX5', 'R3')

r1.add_interface('G0/1')
r1.add_interface('G0/2')
r2.add_interface('S0/2')
r2.add_interface('S0/1')

r1.add_interface_ip('G0/2', '192.168.1.1')

    

