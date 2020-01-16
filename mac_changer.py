# This is a mac changer used to change mac address for linux systems
import subprocess
import optparse
import re
import colorama
def showmac(interface, bf):
    ifconfig_result = str(subprocess.check_output(["ifconfig", str(interface)]))
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address:
        print(colorama.Fore.GREEN + "\n" + bf + " changing the mac: " + mac_address.group(0) + "\n")
    else:
        print("Unable to read the mac given. are you using lo interface?")

def changeTheMac(interface, mac):
    if not interface and not mac:
        print(colorama.Fore.BLUE + "[-] Enter the arguments please... followed by -h to get help...")
    elif not interface:
        print(colorama.Fore.BLUE + "[-] Interface is not given please add -i \"Interface_name\"")
    elif not mac:
        print(colorama.Fore.BLUE + "[-] mac is not given to be changed please add -m 'xx:xx:xx:xx:xx:xx'")
    else:
        print("Starting change mac...")
        # Deprecated...
        # interface = input("Please the interface name : ")
        # mac = input("Please enter the mac address: ")
        print("[+] Changing mac of ", interface, " to ", mac)
        subprocess.call(["ifconfig", interface, "down"])
        print("[+] " + interface + " is now down...")
        subprocess.call(["ifconfig", interface, "hw", "ether", mac])
        print("[+] " + interface + " mac changed...")
        subprocess.call(["ifconfig", interface, "up"])
        print("[+] " + interface + " is now up...")
        print("Completed!!!")



parser = optparse.OptionParser()
parser.add_option("-i", dest="interface", help="Type the interface name you want")
parser.add_option("-m", dest="mac", help="Give the new MAC as the value")
parser.add_option("--mode", dest="mode", help="Change mode to monitor or vice versa, exact parameter required!")
(opts, args) = parser.parse_args()
if (opts.mode == "monitor"):
    print(colorama.Fore.YELLOW + "changing mode to monitor of the interface...")
    subprocess.call(["airmon-ng", "start",opts.interface])
elif (opts.mode == "managed"):
    print(colorama.Fore.GREEN + "changing mode to managed of the interface...")
    subprocess.call(["airmon-ng", "stop",opts.interface])
else:
    print("no interface change given...")

if (opts.mode == "monitor"):
    print("monitor mode given and change please specify the mon interface to change the mac now aborting....")
elif (opts.mode == "managed"):
    if(not opts.interface):
        print("No Interface!!!!")
    else:
        showmac(opts.interface, "Before")
    changeTheMac(opts.interface, opts.mac)
    if(not opts.interface):
        print("No Interface!!!!")
    else:
        showmac(opts.interface, "After")
else:
    if(not opts.interface):
        print("No Interface!!!!")
    else:
        showmac(opts.interface, "Before")
    changeTheMac(opts.interface, opts.mac)
    if(not opts.interface):
        print("No Interface!!!!")
    else:
        showmac(opts.interface, "After")
