import os

po = "Pick your option: "
devpote = "1. Update to the dev channel"
betapote = "2. Update to the beta channel"
normal = "3. Update to the stable channel"
back = "Go back"

os.system('cls')

option = input (po)
if option in ['1', '2', '3', '4']
break

if option == '1'
import devpote
elif option == '2'
import betapote
elif option == '3'
import normal
elif option == '4'
import back
