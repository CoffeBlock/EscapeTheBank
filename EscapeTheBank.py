import time
import random
import keyboard
import os
import sys

gameover = False
point = 10
secrete = False
wait = True
x = 0 # room
y = 0 # floor
z = 0
location = [x, y]
mapE = "=============================================================================\n==              ==              ==              ==              ==+++++++++==\n==              ==              ==              ==              ==    |    ==\n==              ==              ==              ==              ==    |    ==\n==              ==              ==              ==              ==    |    ==\n============================================================================="
map1 = "=============================================================================\n==      W       ==              ==              ==              ==+++++++++==\n==    ivvvi     ==              ==              ==              ==    |    ==\n==     OOO      ==              ==              ==              ==    |    ==\n==     I I      ==              ==              ==              ==    |    ==\n============================================================================="
map2 = "=============================================================================\n==              ==      W       ==              ==              ==+++++++++==\n==              ==    ivvvi     ==              ==              ==    |    ==\n==              ==     OOO      ==              ==              ==    |    ==\n==              ==     I I      ==              ==              ==    |    ==\n============================================================================="
map3 = "=============================================================================\n==              ==              ==      W       ==              ==+++++++++==\n==              ==              ==    ivvvi     ==              ==    |    ==\n==              ==              ==     OOO      ==              ==    |    ==\n==              ==              ==     I I      ==              ==    |    ==\n============================================================================="
map4 = "=============================================================================\n==              ==              ==              ==      W       ==+++++++++==\n==              ==              ==              ==    ivvvi     ==    |    ==\n==              ==              ==              ==     OOO      ==    |    ==\n==              ==              ==              ==     I I      ==    |    ==\n============================================================================="
map5 = "=============================================================================\n==              ==              ==              ==              ==+++ W +++==\n==              ==              ==              ==              ==  ivvvi  ==\n==              ==              ==              ==              ==   OOO   ==\n==              ==              ==              ==              ==   I I   ==\n============================================================================="
ele1 = False
ele2 = False
ele3 = False
ele4 = False
mapinfo = [
    [z, z, z, z],
    [z, z, z, z],
    [z, z, z, z],
    [z, z, z, z]
]
roominfo = 10
mapx = 0
mapy = 0

def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()

#This code is Contributed by PL VISHNUPPRIYAN


def rangen():
    # nothing = 0
    # dragon = 1
    # dimond = 2
    # secrete = 3
    global mapx
    global mapy
    while not mapy == 4:
        while not mapx == 4:
            mapinfo[mapy][mapx] = random.randrange(0, 3)
            mapx = mapx + 1
        mapy = mapy + 1
        mapx = 0
    mapinfo[random.randrange(0, 4)][random.randrange(0, 4)] = 3



def room():
    # nothing = 0
    # dragon = 1
    # dimond = 2
    # secrete = 3
    global roominfo
    global point
    roominfo = mapinfo[y][x]
    if roominfo == 0:
        os.system("cls")
        print("there is nothing in this room")
        time.sleep(1.5)
    elif roominfo == 1:
        os.system("cls")
        print("Ops...")
        time.sleep(0.5)
        print("a dragon here")
        time.sleep(0.5)
        print("Point - 3")
        time.sleep(1)
        point = point - 3
    elif roominfo == 2:
        os.system("cls")
        print("WOW")
        time.sleep(0.5)
        print("5 points for me")
        time.sleep(0.5)
        print("Point + 5")
        time.sleep(1)
        point = point + 5
        mapinfo[y][x] = 0
    elif roominfo == 3:
        os.system("cls")
        print("Nice there was the secrete!")
        global secrete
        secrete = True
        time.sleep(1.5)
        mapinfo[y][x] = 0

    

def ele1cheack():
    global y
    global ele1
    if ele1:
        y = y + 1
    else:
        print("Do you want to unlock the elevator?")
        if userinput == "w":
            global point
            if point > 3:
                point = point - 3
                ele1 = True
                y = y + 1
        else:
            y = y
def ele2cheack():
    global y
    global ele2
    if ele2:
        y = y + 1
    else:
        print("Do you want to unlock the elevator?")
        if userinput == "w":
            global point
            if point > 3:
                point = point - 3
                ele2 = True
                y = y + 1
def ele3cheack():
    global y
    global ele3
    if ele3:
        y = y + 1
    else:
        print("Do you want to unlock the elevator?")
        if userinput == "w":
            global point
            if point > 3:
                point = point - 3
                ele3 = True
                y = y + 1
def ele4cheack():
    global y
    global ele4   
    if ele4:
        y = y + 1
    else:
        print("Do you want to unlock the elevator?")
        if userinput == "w":
            global point
            if point > 3:
                point = point - 3
                ele4 = True
                y = y + 1

def move():
    global userinput
    global x
    global y
    if userinput == "a":
        if x >= 1:
            x = x - 1
    elif userinput == "d":
        if x <= 3:
            x = x + 1
    elif userinput == "w":
        if y <= 2 and x == 4:
            if y == 0:
                ele1cheack()
            elif y == 1:
                ele2cheack()
            elif y == 2:
                ele3cheack()
        elif y == 3:
            if secrete:
                global gameover
                gameover = True
            else:
                print("You need the secrete to get out")
                time.sleep(1.5)

    elif userinput == "s":
        if y >= 1 and x == 4:
            y = y - 1
    
    elif userinput == "space":
        if not x == 4:
            room()
    os.system('cls')
    

def printmap():
    if y == 0:
        print(mapE)
        print(mapE)
        print(mapE)
        if x == 0:
            print(map1)
        elif x == 1:
            print(map2)
        elif x == 2:
            print(map3)
        elif x == 3:
            print(map4)
        elif x == 4:
            print(map5)
    if y == 1:
        print(mapE)
        print(mapE)
        if x == 0:
            print(map1)
        elif x == 1:
            print(map2)
        elif x == 2:
            print(map3)
        elif x == 3:
            print(map4)
        elif x == 4:
            print(map5)
        print(mapE)
    if y == 2:
        print(mapE)
        if x == 0:
            print(map1)
        elif x == 1:
            print(map2)
        elif x == 2:
            print(map3)
        elif x == 3:
            print(map4)
        elif x == 4:
            print(map5)
        print(mapE)
        print(mapE)
    if y == 3:
        if x == 0:
            print(map1)
        elif x == 1:
            print(map2)
        elif x == 2:
            print(map3)
        elif x == 3:
            print(map4)
        elif x == 4:
            print(map5)
        print(mapE)
        print(mapE)
        print(mapE)

def main():
    global gameover
    while not gameover:
        global userinput
        global location
        if point >= 0:
            userinput = keyboard.read_key()
            move()
            location = [x, y]
            printmap()
            print("Point:", point, "  ", "Secrete:", secrete)
            time.sleep(0.2)
        else:
            gameover = True
def start():
    os.system('cls')
    print("Press SPECE to start")
    global wait
    while wait:
        userinput = keyboard.read_key()
        if userinput == "space":
            wait = False
    for i in range(11):
        time.sleep(random.random())
        progressBar(i,10)
    rangen()
    os.system('cls')
    print(mapE)
    print(mapE)
    print(mapE)
    print(map1)
    print("Pont:", point, "  ", "Secrete:", secrete)
    main()

start()

if secrete and point >= 0:
    os.system("cls")
    print("You WIN!!!")
    time.sleep(2)
if not secrete:
    os.system("cls")
    print("Sorry you loose.")
    time.sleep(2)