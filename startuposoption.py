question = "What OS are you're using right now"
pickoption = "Please pick one of the options by pressing 1 - 4"
linux = "1. Linux"
windows = "2. Windows"
macos = "3. Mac OS - Working in progress"
dontknow = "4. Don't know"

print(question)
print(pickoption)
print(linux)
print(windows)
print(macos)
print(dontknow)

input = input (question)
if input in ['1', '2', '3', '4']
break

if option == '1'
import start
elif option == '2'
import startwindows
elif option == '3'
import startmacos
elif option == '4'
import dontknowos