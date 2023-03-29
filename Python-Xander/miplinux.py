import os
import socket
import signal


ipt = "Your ip address is: "

print (ipt + print(os.system('hostname -i')))

signal.pause()
