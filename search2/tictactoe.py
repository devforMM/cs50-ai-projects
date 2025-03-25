"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    co_x=0
    co_y=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                co_x+=1
            elif  board[i][j]==O:
                co_y+=1
    if co_x>co_y:
        return O
    return X
def actions(board):
    liste=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                liste.append((i,j))
    return liste
    


def result(board, action):
    if action not in actions(board):  # Vérification AVANT la copie
        raise ValueError("Invalid move")
    
    board_copy = copy.deepcopy(board)  # Copier uniquement si l'action est valide
    board_copy[action[0]][action[1]] = player(board)  # Assigner directement le bon joueur
    return board_copy




def winner(board):
    # Vérifier les lignes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]

    # Vérifier les colonnes
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]

    # Vérifier la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    # Vérifier la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None
    


def terminal(board):
    cases=[]
    if winner(board) :
        return True
    else:
        for i in range(3):
            for j in range(3):
               if board[i][j]==EMPTY:
                   return False
    return True



def utility(board):
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    return 0
    


def minimax(board):
    if terminal(board):
        return utility(board)

    best_action = None  # Initialisation du meilleur mouvement

    if player(board) == X:  
        best_value = float('-inf')
        for a in actions(board):
            value = minimax(result(board, a))  # Calcul de la valeur Minimax
            if value > best_value:  # Si c'est un meilleur coup, on met à jour
                best_value = value
                best_action = a

    else:  
        best_value = float('inf')
        for a in actions(board):
            value = minimax(result(board, a))
            if value < best_value:
                best_value = value
                best_action = a

    return best_action
    
