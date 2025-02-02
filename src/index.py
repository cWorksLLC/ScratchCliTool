# ScratchCliTool | v1.0.0
# Made by Letter C (cWorksLLC)
import scratchattach as sa
import maskpass
import webbrowser
import time
# importing needed libaries

username = input("what is your username?: ")
password = maskpass.askpass(prompt="what is your password?: ", mask="*")
project = input("what project you want to connect to? (use project id, optional): ")
# getting user input ↑ | applying user input ↓
print("logging in to user...")
session = sa.login(username, password)
print("connecting to cloud project...")
cloud = session.connect_cloud(project)
# connection script

if session.banned == True:
	print("the account you logged in to was banned. closing in 2 seconds")
	time.sleep(2)
	exit()

if session.new_scratcher == True:
	print("the account you logged in is a new scratcher, so cloud features won't work.")

print(f"hello, {username}.")
print("="*75)
print("type 'cmds' for a list of commands.")
print("type 'help' for a guide.")
print("="*75)
# welcoming script

while True:
	cmd = input(f"{username}/{project}>")

	if cmd == "cmds":
		print("UTILITY COMMANDS:")
		print("cmds - self-explanatory (opens this menu)")
		print("help - opens a placeholder URL for a guide")
		print("sessionID - returns the SessionID ")
		print("cproj - changed current project connection")
		print("exit - exits Termatch")
		print("openprj - opens a project in a new window")
		print("CLOUD COMMANDS:")
		print("NOTE: cloud variables are broken, so i don't know if the commands here work.")
		print("setVariable - sets a value to a cloud variable")
		print("getVariable - returns the value of a cloud variable")
		print("U/A COMMANDS:")
		print("mesCount - returns your message count")
		print("comment - comment something on a project")
		print("follow - follows a user")
		print("love - loves a project")
		print("favorite - favorites a project")
	elif cmd == "help":
		webbrowser.open("https://scratch.mit.edu")
	elif cmd == "sessionID":
		print(session.id)
	elif cmd == "cproj":
		project = input("what project you want to connect to? (use project id): ")
		print("connecting to cloud project...")
		cloud = session.connect_cloud(project)
	elif cmd == "exit":
		break
	elif cmd == "openprj":
		prj = input("what is the project id? ")
		webbrowser.open(f"https://scratch.mit.edu/projects/{prj}/embed")
	elif cmd == "setVariable":
		name = input("what variable to set? ")
		value = input("what is the value? ")
		cloud.set_var(name, value)
	elif cmd == "getVariable":
		name = input("what is the variable's name?")
		cloud.get_var(name)
	elif cmd == "mesCount":
		user = session.connect_linked_user()
		print(user.message_count())
	elif cmd == "comment":
		prj = input("what is the project id? ")
		content = input("what are the comment's contents? ")
		projectcon = session.connect_project(prj)		
		comment = projectcon.post_comment(content)
	elif cmd == "follow":
		user = input("who do you need to follow? ")
		usercon = session.connect_user(user)
		usercon.follow()
	elif cmd == "love":
		prj = input("what is the project id? ")
		projectcon = session.connect_project(prj)
		projectcon.love()
	elif cmd == "favorite":
		prj = input("what is the project id? ")
		projectcon = session.connect_project(prj)
		projectcon.favorite()
	else:
		print("not a valid command.")

	user = session.connect_linked_user()
	user.update() # update the user's stats everytime a command is ran

# command line script