
from ncclient import manager
import xmltodict
import xml.dom.minidom

#create a dictionary for the device parameter. NB: To add multiple device , the below could be saved in another .py and imported here
router = {"host": "192.168.174.100",
          "port": "830",
          "username": "cisco",
          "password": "cisco123"}

# #1 this could also use: netconf_filter = open(file path).read  --> reading from a file on the system
# netconf_filter = "paste the xml yang model for the interface"
# netconf_filter = """
# <filters>
#     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#         <interface>
#             <name>gigabitEthernet2</name>
#         </interface>
#     </interfaces>
#     <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#         <interface>
#             <name>gigabitEthernet2</name>
#         </interface>
#     </interfaces-state>
# </filters>"""


#hostkey_verify=False means it should not use the ssh certificate that was downloaded . in production we will allow it
with manager.connect(host=router["host"], port=router["port"], username=router["username"],
                     password=router["password"], hostkey_verify=False) as router_manager:
    for capability in router_manager.server_capabilities:
        print("*" * 100)
        print(capability)   #it will print out all the capabilities of the device

