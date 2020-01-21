import subprocess
import re
import time
from colorama import Fore as color
s = raw_input("Please enter the address to fetch the ping: ")

print(color.YELLOW + "Please wait for 7 seconds or so...")
stringd = subprocess.check_output(["sudo","python", "network_scanner.py", "-i %s"%s])
time.sleep(1)
print("Arping sent")
stringd = subprocess.check_output(["sudo","python", "network_scanner.py", "-i %s"%s])
time.sleep(5)
print("Arping sent")
stringd = subprocess.check_output(["sudo","python", "network_scanner.py", "-i %s"%s])
print("Arping sent")
print(color.LIGHTCYAN_EX)
print("Results... \n")
print("Mac Address\tIP Address")
yo = re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w \d\d\d.\d\d\d.\d*.\d*", stringd)
for i in yo:
    print(i)
