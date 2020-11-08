#!/usr/bin/env python3
import scapy.all as scapy
import optparse
import os
os.system("clear")
os.system("figlet KARABAGH  IS AZERBAIJAN")
# // scapy.ls(scapy.ARP())
# // scapy.ls(scapy.Ether())

# First step : Arp request
# Second step : Broadcast
# Third step : Response
try:
    def paraser():
        parse_obj = optparse.OptionParser()
        parse_obj.add_option("-i", "--ip-range", dest="iprange", help="-i --ip-range | IP range\n")
        (users_input, arguments) = parse_obj.parse_args()
        if not users_input.iprange:
            print("Please enter ip address \n ")
            os.system("sudo python3 scanner.py --help")
            quit()
        return parse_obj.parse_args()


    def arp(iprange):
        arp_request = scapy.ARP(pdst=iprange)
        return arp_request


    def broadcast():
        broadcast_package = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        return broadcast_package


    def combine(broadcast_package, arp_request):
        combined_package = broadcast_package / arp_request
        return combined_package


    def reformat():
        (user_inputs, arguments) = paraser()
        usr = combine(broadcast(), arp(user_inputs.iprange))
        (ans_list, unans_list) = scapy.srp(usr, timeout=1)
        return ans_list.summary()


    reformat()

except TypeError:
    print("Please enter ip address \n ")
    os.system("sudo python3 scanner.py --help")
    print("Usage : sudo python3 scanner.py -i <ip_address/range>")
