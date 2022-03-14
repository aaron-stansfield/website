import random
import datetime
import os
passnum = 0
passed = 0
row1, row2, row3, row4, row5, row6 = ["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","","",]
row1 = list(row1)
row2 = list(row2)
row3 = list(row3)
row4 = list(row4)
row5 = list(row5)
row6 = list(row6)

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def printrows(h):
    if h >=1:
        print(row1)
        if h >=2:
            print(row2)
            if h >=3:
                print(row3)
                if h >= 4:
                    print(row4)
                    if h >= 5:
                        print(row5)
                        if h == 6:
                            print(row6)
    
def wordchoice():
    global memes
    global word
    global to_array
    global array2
    nowl = datetime.datetime.utcnow()
    #nowl = datetime.now()
    now = nowl.strftime("%d %m %Y")
    now = str(now)
    print("the date is",now,":)")
    random.seed(now)
    output = random.randint(0,1377)
    #print(output)
    
    with open("wordstext.txt", "r") as f:
        words = f.read().splitlines()
    print(words[output])
    word = words[output]

    string = word
    memes = list(string)
    to_array = list(string)
    array2 = list(string)
    #print(array2)
    print("Key:")
    print("Hit = 😂")
    print("Letter Present = 🤔")
    print("Miss = 😔")
    print("choose a five letter word to start smile")
    return word

def addlists():
    if passnum == 1:
        for x in range(5):
            row1[x] = row11[x] + userarray[x]     
    elif passnum == 2:
        for x in range(5):
            row2[x] = row21[x] + userarray[x]
    elif passnum == 3:
        for x in range(5):
            row3[x] = row31[x] + userarray[x]    
    elif passnum == 4:
        for x in range(5):
            row4[x] = row41[x] + userarray[x]
    elif passnum == 5:
        for x in range(5):
            row5[x] = row51[x] + userarray[x]             
    elif passnum == 6:
        for x in range(5):
            row6[x] = row61[x] + userarray[x]

def runtimeprint():
    global row11
    global row21
    global row31
    global row41
    global row51
    global row61
    if passnum == 1:
        row11 = row
        rowmoji(row11)
        addlists()
        if passed == 1:
            printrows(1)
    elif passnum == 2:
        row21 = row
        rowmoji(row21)
        addlists()
        if passed == 1:
            printrows(2)
    elif passnum == 3:
        row31 = row
        rowmoji(row31)
        addlists()
        if passed == 1:
            printrows(3)
    elif passnum == 4:
        row41 = row
        rowmoji(row41)
        addlists()
        if passed == 1:
            printrows(4)
    elif passnum == 5:
        row51 = row
        rowmoji(row51)
        addlists()
        if passed == 1:
            printrows(5)
    elif passnum == 6:
        row61 = row
        rowmoji(row61)
        addlists()
        if passed == 1:
            printrows(6)
        
def complete():
    ucheck = str(input("would you like to share you are score ? (y/n) ;)) "))
    if ucheck == "y" or "n":
        if ucheck == "y":
            if passnum == 1:
                clear()
                print("wording2 v1.1(emoji)", str(passnum)+"/6")
                strip(1)
                print("")
                input("enter to quit the quit :)")
                quit()

            elif passnum == 2:
                clear()
                print("wording2 v1.1(emoji)", str(passnum)+"/6")
                strip(2)
                print("")
                input("enter to quit the quit :)")
                quit()

            elif passnum == 3:
                clear()
                print("wording2 v1.1(emoji)", str(passnum)+"/6")
                strip(3)
                print("")
                input("enter to quit the quit :)")
                quit()
                
            elif passnum == 4:
                clear()
                print("wording2 v1.1(emoji)", str(passnum)+"/6")
                strip(4)
                print("")
                input("enter to quit the quit :)")
                quit()

            elif passnum == 5:
                clear()
                print("wording2 v1.1(emoji)", str(passnum)+"/6")
                strip(5)
                print("")
                input("enter to quit the quit :)")
                quit()

            elif passnum == 6:
                clear()
                print("wording2 v1.1(emoji)", str(passnum)+"/6")
                strip(6)
                print("")
                input("enter to quit the quit :)")
                quit()
 

        elif ucheck == "n":
            print("sadge :(")
            input("press enter to end the end")
            quit()

        else:
            clear()
            print("pls ent er y or n ;(")
            complete()
    print("what")

def rowmoji(rowmo):
    for x in range(5):
        if rowmo[x] == "✓":
            rowmo[x] = "😂"
        elif rowmo[x] == "@":
            rowmo[x] = "🤔"
        elif rowmo[x] == "#":
            rowmo[x] = "😔"

def strip(j):
    global row11
    global row21
    global row31
    global row41
    global row51
    global row61
    if j >= 1:
        row11 = str(row11)
        row11 = row11.replace("[","").replace("'","").replace(",","").replace("]","")
        print(row11)
        if j >= 2:
            row21 = str(row21)
            row21 = row21.replace("[","").replace("'","").replace(",","").replace("]","")
            print(row21)
            if j >= 3:
                row31 = str(row31)
                row31 = row31.replace("[","").replace("'","").replace(",","").replace("]","")
                print(row31)
                if j >= 4:
                    row41 = str(row41)
                    row41 = row41.replace("[","").replace("'","").replace(",","").replace("]","")
                    print(row41)
                    if j >= 5:
                        row51 = str(row51)
                        row51 = row51.replace("[","").replace("'","").replace(",","").replace("]","")
                        print(row51)
                        if j == 6:
                            row61 = str(row61)
                            row61 = row61.replace("[","").replace("'","").replace(",","").replace("]","")
                            print(row61)

def corrcheck():
    for x in range(5):
        if userarray[x] == to_array[x]:
            row[x] = "✓"
        else: row[x] = "#"

def presencecheck():
    global array2
    global y
    for y in range(5):
        for x in range(5):
            if row[x] == "✓":
                pass
            elif userarray[y] == array2[x]:
                row[y] = "@"
                array2[x] = "!"
            else:
                pass

    for x in range(5):
        array2[x] = memes[x]

def corrcheck2():
    for x in range(5):
        if userarray[x] == to_array[x]:
            row[x] = "✓"
        else:
            pass

def turn():
    global row
    global passnum
    global userarray
    row = ["#","#","#","#","#"]
    opcor = 0
    userword = str(input(""))
    if len(userword) == 5:
        string = userword
        userarray = list(string)
        clear()
        corrcheck()
        presencecheck()
        corrcheck2()
        passnum = passnum + 1
    else:
        print("please enter a five letter word")
        turn()

#with open("players.txt","r") as f:
 #   mem = f.readline()
#    mem1 = f.readline()
#    mem2 = f.readline()
#    mem3 = f.readline()
#    print(mem)
#    print(mem1)
#    print(mem2)
#    print(mem3)

#mem = list(mem)
#print(mem[2])
bkso = str(input("pls type :) "))
with open("test.txt","w") as f:
    f.write(bkso)
    
wordchoice()
while passnum < 6:
    turn()
    
    if row[0] == "✓" and row[1] == "✓" and row[2] == "✓" and row[3] == "✓"and row[4] == "✓":
        runtimeprint()
        if passnum == 1:
            print("")
            print("")
            printrows(1)
            print("u did it in a single try! :)) (sussy)")
        elif passnum == 2:
            print("")
            print("")
            printrows(2)
            print("u did it in", passnum, "tries :)")
        elif passnum == 3:
            print("")
            print("")
            printrows(3)
            print("u did it in", passnum, "tries :)")
        elif passnum == 4:
            print("")
            print("")
            printrows(4)
            print("u did it in", passnum, "tries :)")
        elif passnum == 5:
            print("")
            print("")
            printrows(5)
            print("u did it in", passnum, "tries :)")
        elif passnum == 6:
            print("")
            print("")
            printrows(6)
            print("u did it in", passnum, "tries :)")     
        complete()
    else:
        pass

    passed = 1
    
    runtimeprint()

    passed = 0
print("6 attempts; You lost :pensive:")
