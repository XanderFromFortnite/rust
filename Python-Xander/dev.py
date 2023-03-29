## Import stuff
import os
## Text
q1 = "These stuff are still in development, you have been warned"
po = "Please pick a option: "
## User option:
mip = "1. What's my IP?"
## Random
space = "---------------------------------"

os.system('cls')

print(q1)
print(space)
print(mip)

while True:
    option = input (po)
    # check if d1a is equal to one of the strings, specified in the list
    if option in ['1', '2', '3']:
        # if it was equal - break from the while loop
        break
# process the input
if option == "1": 
    import mip
elif option == "2": 
    print ("edit me")
elif option == "3": 
    print ("edit me")
## This was from https://stackoverflow.com/questions/21082037/when-making-a-very-simple-multiple-choice-story-in-python-can-i-call-a-line-to
