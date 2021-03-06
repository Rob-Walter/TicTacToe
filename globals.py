# Positions
boardStartingPointX = 0
boardStartingPointY = 0

#Dimensions
screenWidth = 0
sreenHeight = 0

#Colors
fieldHighLightColor = (235, 180, 52)
fieldPossibleMoveColor = (149, 222, 71)
fieldPossibleBeatColor = (222, 71, 71)

#User
user = None

# Savegame
saveGameNumber = None

#GUI-Manager
buttonTypes = {'ACCEPT': '@accept_buttons' , 'DECLINE' : '@decline_buttons', 'STRENGTH': '@strength_buttons', 'SAVE': '@save_buttons'}
textboxTypes = {'INFO':'@infotext', 'WARN': '@warntext', 'RULES': '@rulestext', 'HEADER': '@headertext', 'DATA': '@datatext', "SAVE":"@saveentry"}
inputTypes = {'NORMAL':'@normalinput', 'PASSWORD': '@passwordinput'}

def setStartingPoints(x,y):
    global boardStartingPointX 
    global boardStartingPointY
    boardStartingPointX = x
    boardStartingPointY = y

def setScreenDimensions(width, height):
    global screenWidth
    global screenHeight
    screenWidth = width
    screenHeight = height

def setUser(username, id):
    global user
    user = {'username': username, 'id': id}

def unsetUser():
    global user
    user = None

def setSaveGameNumber(gamenumber):
    global saveGameNumber
    saveGameNumber = gamenumber

def unsetGameNumber():
    global saveGameNumber
    saveGameNumber = None