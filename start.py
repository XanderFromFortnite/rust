## Import stuff
import os
## Text
wel = "Hello, I'm Xander... Made in Python, How may I help you?"
po = "Please pick a option: "
## User option:
dev = "1. Working-in-progress builds"
csoon = "2. COMING SOON"
cal = "3. Calculator"
mip = "4. What is my ip address?"
## Random
space = "---------------------------------"

os.system('clear')

print(wel)
print(space)
print(dev)
print(csoon)
print(cal)
print(mip)

while True:
    option = input (po)
    # check if d1a is equal to one of the strings, specified in the list
    if option in ['1', '2', '3', '4']:
        # if it was equal - break from the while loop
        break
# process the input
if option == "1":
    import dev
elif option == "2":
    import csoon
elif option == "3":
    import cal
elif option == "4":
    import mip
    
## This was from https://stackoverflow.com/questions/21082037/when-making-a-very-simple-multiple-choice-story-in-python-can-i-call-a-line-to
