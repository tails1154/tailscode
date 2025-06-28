import os
import sys
import time

version = "1.0.0"
branch = "dev"
var1 = ""
var2 = ""
var3 = ""
print("TailsCode v" + version + "-" + branch)
running = True
fileloaded = False
commandlist = []
os.system('clear')
print("TailsCode v" + version + "-" + branch)
print("Loading...")
time.sleep(1)

def reloadpointers():
    global commandlist
    commandlist = [False] * 100  # Use 100 slots for demonstration

reloadpointers()
print("TailsCode v" + version + "-" + branch)

def handlecommand(cmd):
    global var1, var2, var3, running, commandlist

    try:
        command = cmd.strip().split()
        if not command:
            return

        if command[0].lower() == "exit":
            running = False

        elif command[0].lower() == "help":
            print("1: print ` <text goes here> `")
            print("1.1: print ` <text goes here> ` <var number>")
            print("2. input <var number (1-3)>")

        elif command[0].lower() == "load":
            if len(command) > 1:
                filename = command[1]
                try:
                    with open(filename, 'rt') as f:
                        print(f"Loading file {filename}...")
                        lines = [line.rstrip('\n') for line in f]
                        reloadpointers()
                        for i, line in enumerate(lines):
                            if i < len(commandlist):
                                commandlist[i] = line
                        print("Loaded!")
                except Exception as ex:
                    print("ERROR loading file")
                    print(ex)
            else:
                print("Filename required. Usage: load <filename>")

        elif command[0].lower() == "save":
            if len(command) > 1:
                filename = command[1]
                try:
                    with open(filename, 'wt') as f:
                        for item in commandlist:
                            if item:
                                f.write(item + "\n")
                        print("Saved!")
                except Exception as ex:
                    print("ERROR saving file!")
                    print(ex)
            else:
                print("Filename required. Usage: save <filename>")

        elif command[0].lower() == "run":
            try:
                for item in commandlist:
                    if item:
                        handlecommand(item)
            except Exception as ex:
                print("ERROR RUNning commands!")
                print(ex)

        elif command[0].lower() == "new":
            try:
                reloadpointers()
                print("New program created.")
            except Exception as ex:
                print("ERROR creating NEW program!")
                print(ex)

        elif command[0].lower() == "del":
            if len(command) > 1 and command[1].isdigit():
                idx = int(command[1])
                if 0 <= idx < len(commandlist):
                    commandlist[idx] = False
                    print(f"Deleted command at line {idx}.")
                else:
                    print("Index out of range.")
            else:
                print("Usage: del <line_number>")

        elif command[0].lower() == "list":
            for idx, item in enumerate(commandlist):
                if item:
                    print(f"{idx}: {item}")

        # Commands that need line numbers
        elif len(command) > 2 and command[1] == "print":
            idx = int(command[0])
            rest = ' '.join(command[2:])
            if rest.startswith("`") and rest.endswith("`"):
                content = rest.strip('`').strip()
                if len(command) > 3 and command[-1] in ("1", "2", "3"):
                    varnum = command[-1]
                    if varnum == "1":
                        print(content + var1)
                    elif varnum == "2":
                        print(content + var2)
                    elif varnum == "3":
                        print(content + var3)
                else:
                    print(content)
                commandlist[idx] = cmd
            else:
                print("No '`' detected! Did you put a space?")

        elif len(command) > 2 and command[1] == "input":
            idx = int(command[0])
            if command[2] in ("1", "2", "3"):
                val = input("? ")
                if command[2] == "1":
                    var1 = val
                elif command[2] == "2":
                    var2 = val
                elif command[2] == "3":
                    var3 = val
                commandlist[idx] = cmd
            else:
                print("Variable number must be 1, 2, or 3.")

        else:
            print("Unknown command. Type 'help' for commands.")

    except Exception as ex:
        print("Command Error")
        print(ex)

def prompt():
    x = input("TailsCode> ")
    handlecommand(x)

while running:
    prompt()