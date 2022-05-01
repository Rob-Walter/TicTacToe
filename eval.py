def evaluate(board):
    twoInARowValue = 10000.0
    threeInARowValue = 25000.0
    fourInARowValue = 400000.0
    centerPosition = 2000.0
    countWhite:int = 0
    score :int = 0
    for columnIndex, column in enumerate(board.fieldArray2D):
        for rowIndex, field in enumerate(column):
            if(field.getPawn() != None):
                pawn = field.getPawn()
                color = pawn.getTeam()
                if(rowIndex > 1 and rowIndex < 4 and columnIndex > 1 and rowIndex < 4):
                    if(color == "white"):
                        score += -centerPosition
                    if(color == "black"):
                        score += centerPosition
                if(rowIndex<3):
                    first = False
                    second = False
                    third = False
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
                            score += -fourInARowValue
                        if(color == "black"):
                            score += fourInARowValue
                    elif (first and second):
                        if(color == "white"):
                            score += -threeInARowValue
                        if(color == "black"):
                            score += threeInARowValue
                    elif(first):
                        if(color == "white"):
                            score += -twoInARowValue
                        if(color == "black"):
                            score += twoInARowValue

                if(columnIndex < 3):
                    first = False
                    second = False
                    third = False
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
                            score += -fourInARowValue
                        if(color == "black"):
                            score += fourInARowValue
                    elif (first and second):
                        if(color == "white"):
                            score += -threeInARowValue
                        if(color == "black"):
                            score += threeInARowValue
                    elif(first):
                        if(color == "white"):
                            score += -twoInARowValue
                        if(color == "black"):
                            score += twoInARowValue
                if(rowIndex<3 and columnIndex <3):
                    first = False
                    second = False
                    third = False
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
                            score += -fourInARowValue
                        if(color == "black"):
                            score += fourInARowValue
                    elif (first and second):
                        if(color == "white"):
                            score += -threeInARowValue
                        if(color == "black"):
                            score += threeInARowValue
                    elif(first):
                        if(color == "white"):
                            score += -twoInARowValue
                        if(color == "black"):
                            score += twoInARowValue

                if(rowIndex>2 and columnIndex <3):
                    first = False
                    second = False
                    third = False
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
                            score += -fourInARowValue
                        if(color == "black"):
                            score += fourInARowValue
                    elif (first and second):
                        if(color == "white"):
                            score += -threeInARowValue
                        if(color == "black"):
                            score += threeInARowValue
                    elif(first):
                        if(color == "white"):
                            score += -twoInARowValue
                        if(color == "black"):
                            score += twoInARowValue
    #score = countBlack - countWhite
    return score

