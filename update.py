import os

pickoption = "Pick your option: "
dev = "1. Update to the dev channel"
beta = "2. Update to the beta channel"
default = "3. Update to the stable channel"
back = "4. Go back"

os.system('cls')

print(pickoption)
print(dev)
print(beta)
print(default)
print(back)


input = input (pickoption)
if input in ['1', '2', '3', '4']
break

if option == '1'
import dev_update
elif option == '2'
import beta_update
elif option == '3'
import default_update
elif option == '4'
import start
