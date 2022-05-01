def evaluate(board):
    countBlack:int = 0
    countWhite:int = 0
    score :int = 0
    for columnIndex, column in enumerate(board.fieldArray2D):
        for rowIndex, field in enumerate(column):
            if(field.getPawn() != None):
                pawn = field.getPawn()  
                color =pawn.getTeam() 
                if(rowIndex<3):
                    first:boolean = False
                    second: boolean = False
                    third: boolean = False
                    if(board.fieldArray2D[columnIndex][rowIndex+1].getPawn()):
                        if(board.fieldArray2D[columnIndex][rowIndex+1].getPawn().getTeam() ==color):
                            first = True
                    if(board.fieldArray2D[columnIndex][rowIndex+2].getPawn()):
                        if(board.fieldArray2D[columnIndex][rowIndex+2].getPawn().getTeam() ==color):
                            second = True
                    if(board.fieldArray2D[columnIndex][rowIndex+3].getPawn()):
                        if(board.fieldArray2D[columnIndex][rowIndex+3].getPawn().getTeam() ==color):
                            third = True               
                    if(first and second and third):
                        if(color == "white"):
                            score += -1000000.0
                        if(color == "black"):
                            score += 1000000.0
                    elif (first and second):
                        if(color == "white"):
                            score += -100000.0
                        if(color == "black"):
                            score += 100000.0
                    elif(first):
                        if(color == "white"):
                            score += -10000.0
                        if(color == "black"):
                            score += 10000.0

                if(columnIndex < 3):
                    first:boolean = False
                    second: boolean = False
                    third: boolean = False
                    if(board.fieldArray2D[columnIndex+1][rowIndex].getPawn()):
                        if(board.fieldArray2D[columnIndex+1][rowIndex].getPawn().getTeam() ==color):
                            first = True
                    if(board.fieldArray2D[columnIndex+2][rowIndex].getPawn()):
                        if(board.fieldArray2D[columnIndex+2][rowIndex].getPawn().getTeam() ==color):
                            second = True
                    if(board.fieldArray2D[columnIndex+3][rowIndex].getPawn()):
                        if(board.fieldArray2D[columnIndex+3][rowIndex].getPawn().getTeam() ==color):
                            third = True               
                    if(first and second and third):
                        if(color == "white"):
                            score += -1000000.0
                        if(color == "black"):
                            score += 1000000.0
                    elif (first and second):
                        if(color == "white"):
                            score += -100000.0
                        if(color == "black"):
                            score += 100000.0
                    elif(first):
                        if(color == "white"):
                            score += -10000.0
                        if(color == "black"):
                            score += 10000.0
                if(rowIndex<3 and columnIndex <3):
                    first:boolean = False
                    second: boolean = False
                    third: boolean = False
                    if(board.fieldArray2D[columnIndex+1][rowIndex+1].getPawn()):
                        if(board.fieldArray2D[columnIndex+1][rowIndex+1].getPawn().getTeam() ==color):
                            first = True
                    if(board.fieldArray2D[columnIndex+2][rowIndex+2].getPawn()):
                        if(board.fieldArray2D[columnIndex+2][rowIndex+2].getPawn().getTeam() ==color):
                            second = True
                    if(board.fieldArray2D[columnIndex+3][rowIndex+3].getPawn()):
                        if(board.fieldArray2D[columnIndex+3][rowIndex+3].getPawn().getTeam() ==color):
                            third = True               
                    if(first and second and third):
                        if(color == "white"):
                            score += -1000000.0
                        if(color == "black"):
                            score += 1000000.0
                    elif (first and second):
                        if(color == "white"):
                            score += -100000.0
                        if(color == "black"):
                            score += 100000.0
                    elif(first):
                        if(color == "white"):
                            score += -10000.0
                        if(color == "black"):
                            score += 10000.0

                if(rowIndex>2 and columnIndex <3):
                    first:boolean = False
                    second: boolean = False
                    third: boolean = False
                    if(board.fieldArray2D[columnIndex+1][rowIndex-1].getPawn()):
                        if(board.fieldArray2D[columnIndex+1][rowIndex-1].getPawn().getTeam() ==color):
                            first = True
                    if(board.fieldArray2D[columnIndex+2][rowIndex-2].getPawn()):
                        if(board.fieldArray2D[columnIndex+2][rowIndex-2].getPawn().getTeam() ==color):
                            second = True
                    if(board.fieldArray2D[columnIndex+3][rowIndex-3].getPawn()):
                        if(board.fieldArray2D[columnIndex+3][rowIndex-3].getPawn().getTeam() ==color):
                            third = True               
                    if(first and second and third):
                        if(color == "white"):
                            score += -1000000.0
                        if(color == "black"):
                            score += 1000000.0
                    elif (first and second):
                        if(color == "white"):
                            score += -100000.0
                        if(color == "black"):
                            score += 100000.0
                    elif(first):
                        if(color == "white"):
                            score += -10000.0
                        if(color == "black"):
                            score += 10000.0
    #score = countBlack - countWhite
    return score
