## Import stuff
import os

os.system('cls')

po = "Type {1} to go back: "
print("I said that this was coming soon...")

while True:
    option = input (po)
    # check if d1a is equal to one of the strings, specified in the list
    if option in ['1']:
        # if it was equal - break from the while loop
        break
# process the input
if option == "1": 
    import start