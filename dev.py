## Import stuff
import os
## Text
q1 = "These stuff are still in development, you have been warned"
po = "Please pick a option: "
## User option:
mip = "1. What's my IP?"
update = "1. Python-Xander updater"
## Random
space = "---------------------------------"

os.system('clear')

print(q1)
print(space)
print(update)

while True:
    option = input (po)
    # check if d1a is equal to one of the strings, specified in the list
    if option in ['1', '2', '3']:
        # if it was equal - break from the while loop
        break
# process the input
if option == "1": 
    import update
## This was from https://stackoverflow.com/questions/21082037/when-making-a-very-simple-multiple-choice-story-in-python-can-i-call-a-line-to
