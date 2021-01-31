import pytest
from router import *

def setup():
    router1 = Router('Cisco', 'IOSv', 'R1')
    router2 = Router('Cisco', '3745', 'R2')
    router3 = Router('Juniper', 'MX5', 'R3')
    router1.add_interface("S0/0")
    router2.add_interface("S0/1")
    router3.add_interface("S0/0")
    return router1, router2, router3

def test_add_interface():
    router1, router2, router3 = setup()
    ans1 = {'S0/0': {'IP': 'unassign', 'Connect': '-'}}
    ans2 = {'S0/1': {'IP': 'unassign', 'Connect': '-'}}
    ans3 = {'S0/0': {'IP': 'unassign', 'Connect': '-'}}
    assert router1.interface == ans1
    assert router2.interface == ans2
    assert router3.interface == ans3

def test_add_interface_ip():
    router1, router2, router3 = setup()
    router1.add_interface_ip("S0/0", "1.1.1.1")
    router2.add_interface_ip("S0/1", "2.2.2.2")
    router3.add_interface_ip("S0/0", "5.5.5.5")
    ans1 = {'S0/0': {'IP': '1.1.1.1', 'Connect': '-'}}
    ans2 = {'S0/1': {'IP': '2.2.2.2', 'Connect': '-'}}
    ans3 = {'S0/0': {'IP': '5.5.5.5', 'Connect': '-'}}
    assert router1.interface == ans1
    assert router2.interface == ans2
    assert router3.interface == ans3

def test_change_hostname():
    router1, router2, router3 = setup()
    router1.change_hostname("NEW")
    assert router1.hostname == "NEW"

def test_connect():
    router1, router2, router3 = setup()
    router1.add_interface_ip("S0/0", "1.1.1.1")
    router2.add_interface_ip("S0/1", "2.2.2.2")
    router1.connect("S0/0", router2, "S0/1")
    ans1 = {'S0/0': {'IP': '1.1.1.1', 'Connect': 'R2 interface : S0/1'}}
    ans2 = {'S0/1': {'IP': '2.2.2.2', 'Connect': 'R1 interface : S0/0'}}
    assert router1.interface == ans1
    assert router2.interface == ans2

def test_show():
    router1, router2, router3 = setup()
    router1.add_interface_ip("S0/0", "1.1.1.1")
    router1.connect("S0/0", router2, "S0/1")
    ans1 = {'brand': 'Cisco', 'model': 'IOSv', 'hostname': 'R1', 'interface': {'S0/0': {'IP': '1.1.1.1', 'Connect': 'R2 interface : S0/1'}}}
    assert router1.__dict__ == ans1

def test_show_interface():
    router1, router2, router3 = setup()
    router1.add_interface_ip("S0/0", "1.1.1.1")
    router1.connect("S0/0", router2, "S0/1")
    assert len(router1.interface) == 1
    assert router1.interface["S0/0"] == {'IP': '1.1.1.1', 'Connect': 'R2 interface : S0/1'}

def test_show_neighbor():
    router1, router2, router3 = setup()
    router1.add_interface_ip("S0/0", "1.1.1.1")
    router1.connect("S0/0", router2, "S0/1")
    assert router1.interface["S0/0"]["Connect"] == "R2 interface : S0/1"




    
