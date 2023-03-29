import os
import socket
import signal


ipt = "Your ip address is: "

print (ipt)
(os.system('hostname -i'))

signal.pause()
