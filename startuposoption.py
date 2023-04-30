import os
os.system('clear')

question = "What OS are you're using right now?"
pickoption = "Please pick one of the options by pressing 1 - 4"
linux = "1. Linux"
windows = "2. Windows - Working in progress"
macos = "3. Mac OS - Working in progress"
dontknow = "4. Don't know"
option = "Option = "

print(question)
print(pickoption)
print(linux)
print(windows)
print(macos)
print(dontknow)

while True:
    option = input (option)
    if option in ['1', '2', '3', '4']:
        break

if option == "1":
    import start
elif option == "2":
    import csoonoteforosoption
elif option == "3":
    import csoonoteforosoption
elif option == "4":
    import csoonoteforosoption