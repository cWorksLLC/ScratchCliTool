# ScratchCliTool | v1.1.0
# Made by Letter C (cWorksLLC) and Webbrowser11 (T_cat9000_2)
import scratchattach as sa # Scratchattach; Help: https://github.com/TimMcCool/scratchattach
import maskpass
import webbrowser
import time

username = input("Enter your username: ")
password = maskpass.askpass(prompt="Enter your password?: ", mask="●")
project = input("What project you want to connect to use id: ")
# getting user input ↑ | applying user input ↓
try:
	print("Logging you in...")
	session = sa.login(username, password)
except Exception as e:
	print(f"An error occured while logging you in: {e}")

try:
	print("Connecting to the cloud...")
	cloud = session.connect_cloud(project)
except Exception as e:
	print(f"An error occured while connecting to the cloud: {e}")

if session.banned == True:
	print("The account you logged into was banned. Closing in 2 seconds.")
	time.sleep(2)
	exit()

if session.new_scratcher == True:
	print("The account you logged in is a new scratcher, so cloud features won't work.")

print(f"Hello, {username}.")
print("="*75)
print("Type 'cmds' for a list of commands.")
print("Type 'help' for a guide.")
print("="*75)
# welcoming script

while True:
	cmd = input(f"{username}/{project}>")

	if cmd == "cmds":
		print("COMMANDS:")
		print("cmds - opens this menu")
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
		print("unlove - unloves a project")
		print("unfavorite - unfavorites a project")
	elif cmd == "help":
		webbrowser.open("https://en.scratch-wiki.info/wiki/Cloud_Data")
	elif cmd == "sessionID":
		print(session.id)
	elif cmd == "cproj":
		project = input("What project you want to connect to? (use project id): ")
		print("Connecting to the cloud...")
		cloud = session.connect_cloud(project)
	elif cmd == "exit":
		break
	elif cmd == "openprj":
		prj = input("Enter the project id: ")
		webbrowser.open(f"https://scratch.mit.edu/projects/{prj}/embed")
	elif cmd == "setVariable":
		name = input("Variable to set? ")
		value = input("Enter value: ")
		cloud.set_var(name, value)
	elif cmd == "getVariable":
		name = input("What is the variable's name?")
		cloud.get_var(name)
	elif cmd == "mesCount":
		user = session.connect_linked_user()
		print(user.message_count())
	elif cmd == "comment":
		prj = input("Please provide the project id: ")
		content = input("Enter the comment content: ")
		projectcon = session.connect_project(prj)		
		comment = projectcon.post_comment(content)
	elif cmd == "follow":
		user = input("Enter username of the person you wish to follow: ")
		usercon = session.connect_user(user)
		usercon.follow()
	elif cmd == "love":
		prj = input("Please provide the project id: ")
		projectcon = session.connect_project(prj)
		projectcon.love()
	elif cmd == "favorite":
		prj = input("Please provide the project id: ")
		projectcon = session.connect_project(prj)
		projectcon.favorite()
	elif cmd == "unlove":
		prj = input("Please provide the project id: ")
		projectcon = session.connect_project(prj)
		projectcon.unlove()
	elif cmd == "unfavorite":
		prj = input("Please provide the project id: ")
		projectcon = session.connect_project(prj)
		projectcon.unfavorite()
	else:
		print("Not a valid command.")

	user = session.connect_linked_user()
	user.update() # update the user's stats everytime a command is ran
