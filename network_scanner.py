import scapy.all as scapy
import optparse
from colorama import Fore as color
def scan(ip):
    print(color.RED)
    scapy.arping(ip)



optp = optparse.OptionParser()
optp.add_option("-i", dest="ip", help="Type the IP address or gateway")
(opts, args) = optp.parse_args()
if (opts.ip):
	scan(opts.ip + "/24")
else:
	print(color.RED + "No IP!")
	print("Type -i \"YOUR_IP\" to set IP or gateway")

