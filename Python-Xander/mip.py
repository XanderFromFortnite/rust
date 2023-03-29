import os
os.system('cls')

print("What device are you on?")
print ("1. Windows")
print("2. Linux")
print("3. MacOS")
print("4. Go Back")


po = "Please pick a option: "

while True:
    option = input (po)
    # check if d1a is equal to one of the strings, specified in the list
    if option in ['1', '2', '3', '4']:
        # if it was equal - break from the while loop
        break
# process the input
if option == "1":
    import mipwindows
elif option == "2":
    import miplinux
elif option == "3":
    import mipmacos
elif option == "4":
    import start
## This was from https://stackoverflow.com/questions/21082037/when-making-a-very-simple-multiple-choice-story-in-python-can-i-call-a-line-to