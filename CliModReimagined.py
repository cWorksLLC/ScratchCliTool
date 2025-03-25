import scratchattach as sa
import maskpass
import webbrowser
import time

print(" _______ _______ ______  _______ _______ _______ __  __  _______ _______ _______ ___    __  __ _______ ______")
print("|    ||    ||  _ | | _  ||    ||    || | | | | |    ||    ||    ||  |    | |    | | |_|  ||    ||   |")
print("| _____||    || | || | |_|  ||_  _||    || |_|  | | |_  _||  _  || _  || |    |     ||    || _  || _  |")
print("| |_____ |    || |_||_ |    ||    |  |  | | |    ||    || | | || | | | |")
print("| _____ ||   _|| __ ||    |  |  | |  _||    ||    || |_|  || |_|  |")
print(" _____| ||   _| | | ||  _  ||  _  ||    || | ||_|| ||    ||    ||    | | | ||    |")
print("|_______||_______||___| |_||__| |__| |___||_______||__| |__| |___||_______||_______||_______| |_| |_||_______||______|")


username = input("Enter your username: ")
password = maskpass.askpass(prompt="Enter your password?: ", mask="●")
project = input("What project you want to connect to use id: ")

try:
    print("Logging you in...")
    session = sa.login(username, password)
    user = session.connect_linked_user()
except Exception as e:
    print(f"An error occurred while logging you in: {e}")
    exit()

try:
    print("Connecting to the cloud...")
    cloud = session.connect_cloud(project)
except Exception as e:
    print(f"An error occurred while connecting to the cloud: {e}")
    cloud = None

if session.banned:
    print("The account you logged into was banned. Closing in 2 seconds.")
    time.sleep(2)
    exit()

if session.new_scratcher:
    print("The account you logged in is a new scratcher, so cloud features won't work.")

print(f"Hello, {username}.")
print("=" * 75)
print("Type 'cmds' for a list of commands.")
print("Type 'help' for a guide.")
print("=" * 75)

while True:
    cmd = input(f"{username}/{project}>")

    if cmd == "cmds":
        print("COMMANDS:")
        print("cmds - opens this menu")
        print("help - opens a placeholder URL for a guide")
        print("sessionID - returns the SessionID ")
        print("cproj - changed current project connection")
        print("exit - exits Termatch")
        print("openprj - opens a project in a new window, and must not be copied a link, a project id should be copied instead.")
        print("CLOUD COMMANDS:")
        print("NOTE: cloud variables are broken, so i don't know if the commands here work, it may be guaranteed that these may work sometimes")
        print("setVariable - sets a value to a cloud variable")
        print("getVariable - returns the value of a cloud variable")
        print("U/A COMMANDS:")
        print("mesCount - returns your message count")
        print("comment - comment something on a project, and must respect scratch's TOS")
        print("follow - follows a user")
        print("love - loves a project")
        print("favorite - favorites a project")
        print("unlove - unloves a project")
        print("unfavorite - unfavorites a project (DO NOT ABUSE THIS)")
        print("addStudio - adds a project to a studio")
    elif cmd == "help":
        webbrowser.open("https://en.scratch-wiki.info/wiki/Cloud_Data")
    elif cmd == "sessionID":
        print(session.id)
    elif cmd == "cproj":
        project = input("What project you want to connect to? (use project id): ")
        try:
            print("Connecting to the cloud...")
            cloud = session.connect_cloud(project)
        except Exception as e:
            print(f"Failed to connect to cloud: {e}")
            cloud = None
    elif cmd == "exit":
        break
    elif cmd == "openprj":
        prj = input("Enter the project id: ")
        webbrowser.open(f"https://scratch.mit.edu/projects/{prj}/embed")
    elif cmd == "setVariable" and cloud:
        name = input("Variable to set? ")
        value = input("Enter value: ")
        cloud.set_var(name, value)
    elif cmd == "getVariable" and cloud:
        name = input("What is the variable's name? ")
        print(cloud.get_var(name))
    elif cmd == "mesCount":
        print(user.message_count())
    elif cmd == "comment":
        prj = input("Please provide the project id: ")
        content = input("Enter the comment content: ")
        project_con = session.connect_project(prj)
        project_con.post_comment(content)
    elif cmd == "follow":
        target_user = input("Enter username of the person you wish to follow: ")
        target_user_con = session.connect_user(target_user)
        target_user_con.follow()
    elif cmd == "love":
        prj = input("Please provide the project id: ")
        project_con = session.connect_project(prj)
        project_con.love()
    elif cmd == "favorite":
        prj = input("Please provide the project id: ")
        project_con = session.connect_project(prj)
        project_con.favorite()
    elif cmd == "unlove":
        prj = input("Please provide the project id: ")
        project_con = session.connect_project(prj)
        project_con.unlove()
    elif cmd == "unfavorite":
        prj = input("Please provide the project id: ")
        project_con = session.connect_project(prj)
        project_con.unfavorite()
    elif cmd == "addStudio":
        prj = input("Enter the project ID to add: ")
        studio = input("Enter the studio ID to add it to: ")
        project_con = session.connect_project(prj)
        project_con.add_to_studio(studio)
    else:
        print("Not a valid command.")

    user.update()
