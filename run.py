import router

router1 = router.Router('Cisco', 'IOSv', 'R1')
router2 = router.Router('Cisco', '3745', 'R2')
router3 = router.Router('Juniper', 'MX5', 'R3')

router1.add_interface("S0/0")
router2.add_interface("S0/1")
router1.add_interface("S0/2")
router2.add_interface("S0/2")
router3.add_interface("S0/0")
router3.add_interface("S0/2")

router1.add_interface_ip("S0/0", "1.1.1.1")
router2.add_interface_ip("S0/1", "2.2.2.2")
router1.add_interface_ip("S0/2", "3.3.3.3")
router2.add_interface_ip("S0/2", "4.4.4.4")
router3.add_interface_ip("S0/0", "5.5.5.5")
router3.add_interface_ip("S0/2", "6.6.6.6")

router1.connect("S0/0", router2, "S0/1")
router1.connect("S0/2", router3, "S0/2")
router3.connect("S0/0", router2, "S0/2")

router1.show()
router1.show_interface()
router1.show_neighbor()

router2.show()
router2.show_interface()
router2.show_neighbor()

router3.show()
router3.show_interface()
router3.show_neighbor()

router3.change_hostname("NEW_R3")
router3.show()


