## Import stuff
import os

os.system('clear')

po = "Type 1 to go back: "
print("If you're seeing this message, that mean the devs haven't even started making this option yet")

while True:
    option = input (po)
    # check if d1a is equal to one of the strings, specified in the list
    if option in ['1']:
        # if it was equal - break from the while loop
        break
# process the input
if option == "1": 
    import start