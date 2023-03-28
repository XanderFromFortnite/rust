wel = "Hello, I'm Xander... Made in Python, How may I help you?"
po = "Please pick a option: "
## User option:
dev = "1. Working-in-progress builds"
## Random
space = "---------------------------------"

print(wel)
print(space)
print(dev)
while True:
    option = input (po)
    # check if d1a is equal to one of the strings, specified in the list
    if option in ['1', '2']:
        # if it was equal - break from the while loop
        break
# process the input
if option == "1": 
    print ("edit me") 
elif option == "2": 
    print ("edit me")
elif option == "3": 
    print ("edit me")
## This was from https://stackoverflow.com/questions/21082037/when-making-a-very-simple-multiple-choice-story-in-python-can-i-call-a-line-to
