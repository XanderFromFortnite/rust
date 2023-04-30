import os

pickoption = "Pick your option: "
dev = "1. Update to the dev channel"
beta = "2. Update to the beta channel"
default = "3. Update to the stable channel"
back = "4. Go back"

os.system('clear')

print(dev)
print(beta)
print(default)
print(back)

while True:
    option = input (pickoption)
    if option in ['1', '2', '3', '4']:
        break

if option == "1":
    import csoonote
elif option == "2":
    import csoonote
elif option == "3":
    import csoonote
elif option == "4":
    import start
