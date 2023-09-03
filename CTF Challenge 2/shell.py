import os

print("WELCOME TO THE UPPERCASE SHELL")
print("All your commands will be converted to uppercase...")
print("Can you escape it?")
print("type 'exit' or use Ctrl+C to quit")
print("---------------------------------")

usrInput = input("UpperCaseShell> ")

while usrInput != "exit":
	usrInput = usrInput.upper()
	os.system(usrInput)
	usrInput = input("UpperCaseShell> ")
