import os
import sys
import time

version="1.0.0"
branch="dev"
print("TailsCode v" + version + "-" + branch)
running=True
f=False
fileloaded=False
commandlist=[]
pointer=0
os.system('clear')
print("TailsCode v" + version + "-" + branch)
print("Loading...")
time.sleep(1)
def reloadpointers():
    pointer=0
    while pointer!=99999:
        print(str(pointer) + "/99999")
        commandlist.append(False)
        pointer=pointer+1
    os.system('clear')
reloadpointers()
print("TailsCode v" + version + "-" + branch)
def handlecommand(cmd):
    try:
        global running
        global f
        command=cmd.split(" ")
        if command[0]=="exit":
            running=False
        elif command[0]=="load":
            try:
                if command[1]:
                    print("Loading file " + command[1] + "...")
                    f = open(command[1], 'rt')
                    ftext=f.read()
                    pointer=0
                    reloadpointers()
                    for line in ftext:
                        commandlist[pointer]=line
                        pointer=pointer+1
                    ftext=False
                    f.close()
            except Exception as ex:
                print("ERROR loading file")
                print(ex)
        elif command[0]=="save":
            try:
                if command[1]:
                    print("Saving to file " + command[1] + "...")
                    f = open(command[1], 'wt')
                    pointer=0
                    for item in commandlist:
                        if item != False:
                            if pointer != 0:
                                f.write("\n")
                            f.write(item)
                            pointer=pointer+1
                    f.close()
                    print("Saved!")
            except Exception as ex:
                print("ERROR saving file!")
                print(ex)
        elif command[0]=="run":
            try:
                for item in commandlist:
                    if item != False:
                        handlecommand(item)
            except Exception as ex:
                print("ERROR RUNning commands!")
                print(ex)
        elif command[1]=="print":
            # print("print command called")
            try:
                pointer=0
                commandlist[int(command[0])]=cmd
                # print(command[2])
                if command[2]=="`":
                    try:
                        pointer=0
                        string=""
                        # print("FOR loop about to start!")
                        for item in command:
                            # print(item)
                            if pointer!=0:
                                if pointer!=1:
                                    if pointer!=2:
                                        if item!="`":
                                            # print("new item: " + str(item))
                                            string = string + item
                            if pointer!=2:
                                if item == "`":
                                    break
                            pointer=pointer+1
                        print(string)
                    except Exception as ex:
                        print("Syntax error: Never ending string")
                        print(ex)
                else:
                    print("No '`' detected! did you put a space?")
            except Exception as ex:
                print("Syntax error at value 2: String Expected")
                print(ex)
    except Exception as ex:
        print("Command Error")
        print(ex)

def prompt():
    global running
    global f
    x=input("TailsCode>")
    handlecommand(x)

while running:
    prompt()
