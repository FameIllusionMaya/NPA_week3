"""NPA week3 homework define python class for router"""

class Router:
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interface = {}

    def add_interface(self, interface):
        """add interface to router"""
        self.interface[interface] = {"IP" : "unassign", "Connect" : "-"}

    def add_interface_ip(self, interface, ip):
        """assign ip to an interface"""
        self.interface[interface]["IP"] = ip

    def change_hostname(self, new_name):
        """change hostname"""
        self.hostname = new_name


    def connect(self, interface_1, device, interface_2):
        """connect device with another in topology graph"""
        self.interface[interface_1]["Connect"] = device.hostname + " interface : " + interface_2
        device.interface[interface_2]["Connect"] = self.hostname + " interface : " + interface_1

    def show(self):
        info = self.__dict__
        print("----- Show all configue -----")
        for att in info:
            print(att + " : " + str(info[att]))

    def show_interface(self):
        """show interface information IP and connecting"""
        print("----- Show interface -----")
        print("Router : ", self.hostname)
        print("Interface amount : ", len(self.interface))
        for att in self.interface:
            print("Interface : ", att)
            print("IP address : ", self.interface[att]["IP"])

    def show_neighbor(self):
        print("----- Show neighbor -----")
        print("Router : ", self.hostname)
        for att in self.interface:
            print("Neighbor : ", self.interface[att]["Connect"])
