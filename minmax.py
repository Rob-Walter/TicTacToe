from copy import deepcopy
from locale import currency
from board import Board

import pygame

#position -> der Status des Boards also die Position der Steine
#depth -> wie tief man in den Tree vordringt (die bestmöglichen Züge vorraussagen)
#maximizing_player -> boolean | gucken ob maximieren oder minimieren | wenn maximizing_player = false => minimieren
#game -> ist das Game was gespielt wird
def minimax(initialBoard, initialMove, depth, maximizing_player): #alpha, beta

    # board.is_human_turn = not maximizing_player
    # children = board.get_all_possible_moves()

#erstmal testen ob das Game noch läuft bzw. vorbei ist
    winOrDrawCheck = initialBoard.checkForWinOrDraw(True)
    if depth == 0 or winOrDrawCheck[0] == "win" or winOrDrawCheck[0] == "draw":
        score = initialBoard.evaluate()
        if maximizing_player:
            score -= depth * 1000
        else:
            score += depth * 1000
        return initialBoard, score,  initialMove

    

    if maximizing_player:
        max_eval = float('-inf') #für den MaxPlayer ist negative Unendlichekit (-inf) am besten
        best_board = None
        bestmove = None
        for move in get_all_moves(initialBoard, "black"): #Die Ki ist immer Schwarz
            
            current_eval = minimax(move[0],move[1], depth - 1, False)
            #print("current - max",current_eval)

            max_eval = max(max_eval, current_eval[1])
            
            if current_eval[1] == max_eval:
                max_eval = current_eval[1]
                best_board = move[0]
                bestmove = move[1]
        return best_board, max_eval,  bestmove

    else:
        min_eval = float('+inf') #für den MinPlayer ist positive Unendlichekit (+inf) am besten
        best_board = None
        bestmove = None
        for move in get_all_moves(initialBoard, "white"): #Der Player ist immer weiß
            current_eval = minimax(move[0],move[1], depth - 1, True)
            #print("current - min",current_eval)
            min_eval = min(min_eval, current_eval[1])
            if current_eval[1] == min_eval:
                min_eval = current_eval[1]
                best_board = move[0]
                bestmove = move[1]
        return best_board, min_eval, bestmove


def simulate_move( move, board, color):
    board.move(move, color)
    return board

#herausfinden wo alle steine stehen und deren möglichen Züge rausfinden
def get_all_moves(board, color):
    moves = []
    valid_moves = board.checkPossibleMovesComp() #(row, col): [pieces]
    for item in valid_moves:
        if(item):
            for move in item:
                for rowIndex, column in enumerate(board.fieldArray2D):
                    for columnIndex, field in enumerate(column):
                        field.unsetSurface()
                        if(field.getPawn()!=None):
                            field.getPawn().unsetSprite()

                temp_surface = board.surface
                board.surface = None
                temp_board = deepcopy(board) # immer ein neues Board "erstellen" 
                for rowIndex, column in enumerate(board.fieldArray2D):
                    for columnIndex, field in enumerate(column):
                        field.setSurface()
                        if(field.getPawn()!=None):
                            field.getPawn().setSprite()
                board.surface = temp_surface
                new_board = simulate_move(move, temp_board, color)
                moves.append((new_board,move))
    return moves



 # alpha = max(alpha, current_eval)
            # if beta <= alpha:
            #     break