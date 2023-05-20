#Importing the time variable to use for for sleep functions, as well as initializing my variables
import time

haswon = False

usercoord = [7, 0]
limits = [15, 15]
limits2 = [-1, -1]

curTile = 7
isWall =   [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1,
            1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1,
            1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1,
            1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1,
            1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0,
            1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1,
            1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
            1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0,
            1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0,
            1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0,
            1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0,
            1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1,
            0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1]

currentroom = ""

directions = {
    "north":[0, 1],
    "south":[0, -1],
    "east":[1, 0],
    "west":[-1, 0]
}

'''
Commented out for me to remember which coordinates correspond with which room
keyroom = [1,1]
axroom = [13,2]
princessroom = [14,12]
hedgeroom = [0,14]
exitroom = [12,14]
'''

roomnum = {
    str([1,1]):0,
    str([13,2]):1,
    str([14,12]):2,
    str([0,14]):3,
    str([12,14]):4
}

usinv = []
mapinv = [["key"], ["ax"], ["princess"], [], []]

items ={
    "key":"a shiny golden key",
    "ax":"a broad felling ax",
    "princess":"a fair maiden"
}

#This function allows the messages to be typed out in front of the user, instead of appearing all at once.
def printf(message):
    for letter in message:
        print(letter, end = '', flush = True)
        time.sleep(0.04)
    print("")

#This function uses two if statements to check if the user's desired direction is not outside the limits of the map.
def movement(usercoord, response, limits, limits2):
    try:
        movevalues = directions[response[1]]
        if (usercoord[0] + movevalues[0]) == limits[0]:
            printf("You have reached an impenetrable wall of ivy. You cannot travel any further in this direction.")
            time.sleep(0.8)
        elif (usercoord[0] + movevalues[0]) == limits2[0]:
            printf("You have reached an impenetrable wall of ivy. You cannot travel any further in this direction.")
            time.sleep(0.8)
        else:
            usercoord[0] += movevalues[0]

        if (usercoord[1] + movevalues[1]) == limits[1]:
            printf("You have reached an impenetrable wall of ivy. You cannot travel any further in this direction.")
            time.sleep(0.8)
        elif (usercoord[1] + movevalues[1]) == limits2[1]:
                printf("You have reached an impenetrable wall of ivy. You cannot travel any further in this direction.")
                time.sleep(0.8)
        else:
            usercoord[1] += movevalues[1]
            
    except:
        printf("What direction is that?")
        time.sleep(0.8)

#This function is used to pick up items in different key rooms around the map
def pickup(usinv, mapinv, currentroom):
    try:
        item = mapinv[currentroom]
        usinv += item
        mapinv[currentroom] = ''
    except:
        printf("You can't find that in the area.")
        time.sleep(0.8)

#This function checks the array of values called isWall, and compares it to the coordinates that the player would be at. If there is a wall, then they cannot move.
def wallCheck(response, curTile, usercoord, isWall, limits, limits2):
    if response[1] == "north":
        try:
            if isWall[curTile+15]:
                printf("There is an impenetrable hedge wall in your way.")
            else: 
                movement(usercoord, response, limits, limits2)
        except:
            printf("You cannot go this way.")
            time.sleep(0.8)

    elif response[1] == "south":
        try:
            if isWall[curTile-15]:
                printf("There is an impenetrable hedge wall in your way.")
            else:
                movement(usercoord, response, limits, limits2)
        except:
            printf("You cannot go this way.")
            time.sleep(0.8)

    elif response[1] == "east":
        try:
            if isWall[curTile+1]:
                printf("There is an impenetrable hedge wall in your way.")
            else:
                movement(usercoord, response, limits, limits2)
        except:
            printf("You cannot go this way.")
            time.sleep(0.8)
            
    elif response[1] == "west":
        try:
            if isWall[curTile-1]:
                printf("There is an impenetrable hedge wall in your way.")
            else:
                movement(usercoord, response, limits, limits2)
        except:
            printf("You cannot go this way.")
            time.sleep(0.8)

    else:
        printf("Where did you want to go?")
        time.sleep(0.8)

#This functions handles the messages displayed when you enter different rooms throughout the maze. It also has a way of telling the player which direction they can go.
def roomTalk(currentroom, curTile, isWall, mapinv):
    if currentroom == 0:
        if mapinv[currentroom] == "":
            printf("You are surrounded by hedges on all sides except for the one you entered through.")
            time.sleep(0.8)
        else:
            printf("You are surrounded by hedges on all sides except for the one you entered through. There is a key on the ground.")
            time.sleep(0.8)
    elif currentroom == 1:
        if mapinv[currentroom] == "":
            printf("You are surrounded by hedges on all sides except for the one you entered through.")
            time.sleep(0.8)
        else:
            printf("You are surrounded by hedges on all sides except for the one you entered through. There is an ax on the ground.")
            time.sleep(0.8)
    elif currentroom == 2:
        if mapinv[currentroom] == "":
            printf("You are surrounded by hedges on all sides except for the one you entered through.")
            time.sleep(0.8)
        else:
            printf("You are surrounded by hedges on all sides except for the one you entered through. There is a princess lying tied up on the ground.")
            time.sleep(0.8)
    elif currentroom == 3:
        printf("You are surrounded by hedges on all sides except for the one you entered through. The hedges here are thin and could be cut through...")
        time.sleep(0.8)
    elif currentroom == 4:
        printf("You are surrounded by hedges on all sides except for the one you entered through. In front of you lies a wrought iron gate.")
        time.sleep(0.8)
    else:
        listdirs = []
        y = ""
        try:
            if isWall[curTile+15] == 0:
                listdirs.append("North")
        except:
            pass
        try:
            if isWall[curTile-15] == 0:
                listdirs.append("South")
        except:
            pass
        try:
            if isWall[curTile+1] == 0:
                listdirs.append("East")
        except:
            pass
        try:
            if isWall[curTile-1] == 0:
                listdirs.append("West")
        except:
            pass
        printf("You are currently in a hallway surrounded by hedges. You can go:")
        for y in listdirs:
            print(y)
        
#Beginning message
printf("You are an intrepid explorer mapping out the Amazon jungle. You found a hedge maze, quite out of place I know, and decided to explore it. As soon as you stepped inside, the entrance closed up behind you and you found yourself trapped. Now you must find your way out...")
time.sleep(5)

#As long as the player hasn't won yet, it loops
while(haswon == False):

    print("\n\n\n")

    #Checks if the player is currently in any of the special rooms.
    try:
        currentroom = roomnum[str(usercoord)]
    except:
        pass
    
    #Typing out the preamble for the hallways, and then asking for user input. Also, lowercasing the user input to use with if statements.
    roomTalk(currentroom, curTile, isWall, mapinv)

    time.sleep(0.8)
    printf("What do you want to do?")
    response = input().split()

    response[0] = response[0].lower()
    response[1] = response[1].lower()

    #Depending on the response, the code will go to different functions
    try:
        if response[0] == "go":
            wallCheck(response, curTile, usercoord, isWall, limits, limits2)
        elif response[0] == "take":
            pickup(usinv, mapinv, currentroom)
        elif response[0] == "inventory":
            #Iterating through all of the items the player has and typing it out.
            printf("You currently have: ")
            for x in usinv:
                print(items[x])
            print("\nin your inventory.")
            time.sleep(0.8)
        elif response[0] == "unlock" and response[1] == "gate" and currentroom == 4:
            #If the player unlocks the gate, they win
            for w in usinv:
                if w == "key":
                    haswon = True
        elif response[0] == "cut" and response[1] == "hedge" and currentroom == 3:
            #If they cut through the hedges, they win
            for w in usinv:
                if w == "ax":
                    haswon = True
    except:
        pass
    
    #Resetting variables
    currentroom = ""
    curTile = usercoord[0] + (usercoord[1]*15)
    w = ""
print("/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n/n")
#Plays the winning statement
printf("You have escaped the maze!!")
time.sleep(1)
print("/n")

#If you explored and found the princess you get a special line of text
for w in usinv:
    if w == "princess":
        printf("You live out the rest of your life happily with the fair maiden you rescued.")
time.sleep(3)