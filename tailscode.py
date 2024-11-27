import os
import sys
import time

version="1.0.0"
branch="dev"
var1=""
var2=""
var3=""
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
        global var1
        global var2
        global var3
        global running
        global f
        command=cmd.split(" ")
        if command[0].lower()=="exit":
            running=False
        elif command[0].lower()=="load":
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
        elif command[0].lower()=="save":
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
        elif command[0].lower()=="run":
            try:
                for item in commandlist:
                    if item != False:
                        handlecommand(item)
            except Exception as ex:
                print("ERROR RUNning commands!")
                print(ex)
        elif command[0].lower()=="new":
            try:
                reloadpointers()
            except:
                print("ERROR creating NEW program (how? make a bug report if you see this!)")
                print("I will try again when you press enter")
                input()
                reloadpointers()
        elif command[0].lower()=="del":
            try:
                # print(commandlist[command[1]])
                commandlist[int(command[1])]=False
            except Exception as ex:
                print("Could not DELete line!")
                print(ex)
        elif command[0].lower()=="list":
            try:
                for item in commandlist:
                    if item!=False:
                        print(item)
                        print("\n")
            except:
                print("Could not LIST commands!")
        #
        #
        #
        #
        #    commands that need line numbers!!!
        #
        #
        #
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
                                            if pointer != 3:
                                                string = string +  " " + item
                                            else:
                                                string = string + item
                            if pointer!=2:
                                if item == "`":
                                    break
                            pointer=pointer+1
                        try:
                            if command[pointer+1]:
                                if command[pointer+1]=="1":
                                    print(string + var1)
                                elif command[pointer+1]=="2":
                                    print(string + var2)
                                elif command[pointer+1]=="3":
                                    print(string + var3)
                                else:
                                    print("Syntax error: not a usable variable or none selected")
                        except Exception as ex:
                            print(string)
                    except Exception as ex:
                        print("Syntax error: Never ending string")
                        print(ex)
                else:
                    print("No '`' detected! did you put a space?")
            # except Exception as ex:
                # print("Command error!")
                # print(ex)
            except Exception as ex:
                print("Syntax error at value 2: String Expected")
                print(ex)
        elif command[1]=="input":
            try:
                pointer=0
                commandlist[int(command[0])]=cmd
                if command[2]=="1":
                    var1=input("?")
                elif command[2]=="2":
                    var2=input("?")
                elif command[2]=="3":
                    var3=input("?")
                else:
                    raise Exception
            except Exception as ex:
                print("input command error!")
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
