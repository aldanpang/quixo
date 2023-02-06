# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:30:13 2021

@author: aldan
"""
import numpy as np
import random
import math


def check_move(board, turn, index, push_from):
    n = int(math.sqrt(len(board)))
    #PLAYER 1
    if turn == 1:
        if board[index] == 0:
            #Push from Right
            if push_from == 'R':
                #Right pieces 4, 9, 14, 19
                if (index + 1) % n == 0:
                    return False
                #Top pieces 
                if 0 <= index <= n-2:
                    if board[index] == 0: 
                        return True
                #Bottom pieces 
                elif n*(n-1) <= index <= (n*n)-2:
                    if board[index] == 0:
                        return True
                #Left pieces 
                elif index % n == 0:
                    if board[index] == 0:
                        return True
                # everything in middle
                else:
                    return False
            #Push from Left    
            elif push_from == 'L':
                #Left pieces
                if index % n == 0:
                    return False
                #Top pieces 1, 2, 3, 4
                elif 1 <= index <= n-1:
                    if board[index] == 0:
                        return True
                #Bottom pieces 21, 22, 23, 24
                elif (n*(n-1))+1 <= index <= (n*n)-1:
                    if board[index] == 0:
                        return True
                #Right pieces 4, 9, 14, 19
                elif (index + 1) % n == 0:
                    if board[index] == 0:
                        return True
                #everything in middle
                else:
                    return False
            #Push from Top    
            elif push_from == 'T':
                #Top pieces
                if 0 <= index <= (n-1):
                    return False
                #Bottom pieces
                elif (n*(n-1)) <= index <= ((n*n)-1):
                    if board[index] == 0:
                        return True
                #Left pieces
                elif index % n == 0:
                    if board[index] == 0:
                        return True
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 0:
                        return True
                #remaining pieces
                else:
                    return False
            
            elif push_from == 'B':
                #Bottom pieces
                if (n*(n-1)) <= index <= ((n*n)-1):
                    return False
                #Top pieces
                elif 0 <= index <= (n-1):
                    if board[index] == 0:
                        return True
                #Left pieces
                elif index % n == 0:
                    if board[index] == 0:
                        return True
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 0:
                        return True
                else:
                    return False
                    
        elif board[index] != 0:
            #push from Left
            if push_from == 'L':
                #Left pieces
                if index % n == 0:
                    return False
                #Top pieces
                if 1 <= index <= (n-1):
                    if board[index] == 1:
                        return True
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 1:
                        return True
                #Bottom pieces
                elif (n*(n-1)) <= index <= ((n*n)-1):
                    if board[index] == 1:
                        return True
                else:
                    return False
            
            #push from Right
            elif push_from == 'R':
                #Right pieces
                if (index + 1) % n == 0:
                    return False
                #Top pieces
                if 0 <= index <= (n-2): 
                    if board[index] == 1:
                        return True
                #Left pieces
                elif index % n == 0:
                    if board[index] == 1:
                        return True
                #Bottom pieces
                elif (n*(n-1)) <= index <= ((n*n)-1):
                    if board[index] == 1:
                        return True
                else:
                    return False
            
            #push from Top
            elif push_from == 'T':
                #Top pieces
                if 0 <= index <= (n-1):
                    return False
                #Bottom pieces
                elif (n*(n-1)) <= index <= ((n*n)-1):
                    if board[index] == 1:
                        return True  
                #Left pieces
                elif index % n == 0:
                    if board[index] == 1:
                        return True
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 1:
                        return True
                    
                    
            #push from Bottom
            elif push_from == 'B':
                #Bottom pieces
                if (n*(n-1)) <= index <= ((n*n)-1):
                    return False
                #Top pieces
                elif 0 <= index <= (n-2): 
                    if board[index] == 1:
                        return True
                #Left pieces
                elif index % n == 0:
                    if board[index] == 1:
                        return True
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 1:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    #PLAYER 2
    if turn == 2:
        if board[index] == 0:
            #Push from Right
            if push_from == 'R':
                #Right pieces 4, 9, 14, 19
                if (index + 1) % n == 0:
                    return False
                #Top pieces 0, 1, 2, 3
                elif 0 <= index <= n-2:
                    if board[index] == 0: 
                        return True
                #Bottom pieces 20, 21, 22 23
                elif n*(n-1) <= index <= (n*n)-2:
                    if board[index] == 0:
                        return True
                #Left pieces 5, 10, 15, 20
                elif index % n == 0:
                    if board[index] == 0:
                        return True
                #Right pieces and everything in middle
                else:
                    return False
            #Push from Left    
            elif push_from == 'L':
                #Left pieces
                if index % n == 0:
                    return False
                #Top pieces 1, 2, 3, 4
                elif 1 <= index <= n-1:
                    if board[index] == 0:
                        return True
                #Bottom pieces 21, 22, 23, 24
                elif (n*(n-1))+1 <= index <= (n*n)-1:
                    if board[index] == 0:
                        return True
                #Right pieces 4, 9, 14, 19
                elif (index + 1) % n == 0:
                    if board[index] == 0:
                        return True
                #everything in middle
                else:
                    return False
            #Push from Top    
            elif push_from == 'T':
                #Top pieces
                if 0 <= index <= (n-1):
                    return False
                #Bottom pieces
                elif (n*(n-1)) <= index <= ((n*n)-1):
                    if board[index] == 0:
                        return True
                #Left pieces
                elif index % n == 0:
                    if board[index] == 0:
                        return True
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 0:
                        return True
                #remaining pieces
                else:
                    return False
            
            elif push_from == 'B':
                #Bottom pieces
                if (n*(n-1)) <= index <= ((n*n)-1):
                    return False
                #Top pieces
                elif 0 <= index <= (n-1):
                    if board[index] == 0:
                        return True
                #Left pieces
                elif index % n == 0:
                    if board[index] == 0:
                        return True
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 0:
                        return True
                else:
                    return False
                    
        elif board[index] != 0:
            #push from Left
            if push_from == 'L':
                #Left pieces
                if index % n == 0:
                        return False
                #Top pieces
                if 1 <= index <= (n-1):
                    if board[index] == 2:
                        return True
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 2:
                        return True
                #Bottom pieces
                elif (n*(n-1)) <= index <= ((n*n)-1):
                    if board[index] == 2:
                        return True
                else:
                    return False
            
            #push from Right
            elif push_from == 'R':
                #Right pieces
                if (index + 1) % n == 0:
                    return False
                #Top pieces
                elif 0 <= index <= (n-2): 
                    if board[index] == 2:
                        return True
                #Left pieces
                elif index % n == 0:
                    if board[index] == 2:
                        return True
                #Bottom pieces
                elif (n*(n-1)) <= index <= ((n*n)-1):
                    if board[index] == 2:
                        return True
                else:
                    return False
            
            #push from Top
            elif push_from == 'T':
                #Top pieces
                if 0 <= index <= (n - 1):
                   return False 
                #Bottom pieces
                elif (n*(n-1)) <= index <= ((n*n)-1):
                    if board[index] == 2:
                        return True
                    else:
                        return False   
                #Left pieces
                elif index % n == 0:
                    if board[index] == 2:
                        return True
                    else:
                        return False
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 2:
                        return True
                    else:
                        return False
                    
            #push from Bottom
            elif push_from == 'B':
                #Bottom pieces
                if (n*(n-1)) <= index <= ((n*n)-1):
                    return False
                #Top pieces
                elif 0 <= index <= (n-2): 
                    if board[index] == 2:
                        return True
                    else:
                        return False
                #Left pieces
                elif index % n == 0:
                    if board[index] == 2:
                        return True
                    else:
                        return False
                #Right pieces
                elif (index + 1) % n == 0:
                    if board[index] == 2:
                        return True
                    else:
                      
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False              


def apply_move(board, turn, index, push_from):
    n = int(math.sqrt(len(board)))
    #player 1
    if turn == 1:
        if push_from == 'B':
            # Push upwards for any entry, dependent on whatever index they input
            a=1
            boardtmp = board[:]
            while index < index + n*a <= (n*n) - 1:
                boardtmp[index + n*a - n] = boardtmp[index + n*a] 
                a += 1
            boardtmp[index + n * (a-1)] = 1  
            board = boardtmp[:]
            return board[:]
        
        if push_from == 'T':
            a = 1
            boardtmp = board[:]
            while index - n*a >=0:
                boardtmp[(index - n*a) + n] = boardtmp[index - n*a]
                a += 1
            boardtmp[index - (n*(a- 1))] = 1
            board = boardtmp[:]
            return board[:]
            
        if push_from == 'L':
            if index in list(range(1, n+1)): #top row
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert(0, 1)
                board = boardtmp[:]
                return board[:]
            
            elif index in list(range((n-1)*n + 1, n*n + 1)): #bottom row
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert((n-1)*n, 1)
                board = boardtmp[:]
                return board[:]
            
            elif index in list(range(2*n-1, (n-1)*n, n)): #everything in between
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert(index - (n-1), 1)
                board = boardtmp[:]
                return board[:]
            
        if push_from == 'R':
            if index in list(range(0, n-1)): #top row
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert(n-1, 1)
                board = boardtmp[:]
                return board[:]
                
            elif index in list(range((n-1)*n, n*n-1)): #bottom row
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert(n*n-1, 1)
                board = boardtmp[:]
                return board[:]
            
            elif index in list(range(n, (n-1)*n, n)): #everything in between
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert(index + (n-1), 1)
                board = boardtmp[:]
                return board[:]

        #player 2
    if turn == 2:
        if push_from == 'B':
            # Push upwards for any entry, dependent on whatever index they input
            a=1
            boardtmp = board[:]
            while index < index + n*a <= (n*n) - 1:  
                boardtmp[index + n*a - n] = boardtmp[index + n*a]
                a += 1
            boardtmp[index + n * (a-1)] = 2  
            board = boardtmp[:]
            return board[:]
        
        if push_from == 'T':
            a = 1
            boardtmp = board[:]
            while index - n*a >=0:
                boardtmp[(index - n*a) + n] = boardtmp[index - n*a]
                a += 1
            boardtmp[index - (n*(a- 1))] = 2
            board = boardtmp[:]
            return board[:]
            
        if push_from == 'L':
            if index in list(range(1, n+1)): #top row
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert(0, 2)
                board = boardtmp[:]
                return board[:]
            
            elif index in list(range((n-1)*n + 1, n*n + 1)): #bottom row
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert((n-1)*n, 2)
                board = boardtmp[:]
                return board[:]
            
            elif index in list(range(2*n-1, (n-1)*n, n)): #everything in between
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert(index - (n-1), 2)
                board = boardtmp[:]
                return board[:]
            
        if push_from == 'R':
            if index in list(range(0, n-1)): #top row
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert(n-1, 2)
                board = boardtmp[:]
                return board[:]
                
            elif index in list(range((n-1)*n, n*n-1)): #bottom row
                boardtmp = board[:]
                boardtmp.pop(index)
                boardtmp.insert(n*n-1, 2)
                board = boardtmp[:]
                return board[:]
            
            elif index in list(range(n, (n-1)*n, n)): #everything in between
                boardtmp = board[:]   
                boardtmp.pop(index)
                boardtmp.insert(index + (n-1), 2)
                board = boardtmp[:]
                return board[:]
  
            
def check_victory(board, who_played):
    n = int(math.sqrt(len(board)))
# return 0 if no winning situation is present for this game
# return 1 if player 1 wins
# return 2 if player 2 wins
    if who_played == 1:
        #horizonally 
        for i in range(0,n):
            if board[(n*i):(n*i)+n] == [2]*(n):
                return 2
                break
            else:
                pass
        #vertically
        for i in range(0, n):
            if board[i:(n*(n-1))+(i+1):n] == [2]*(n):
                return 2
                break
            else:
                pass
        #diagonally
        for i in range(0, n**2, n+1):
            if board[0::n+1] == [2]*(n):
                return 2
                break
            else:
                pass
        for i in range(0, n*(n-1)+1, n-1):
            if board[n-1:(n*n)-(n-1):(n-1)] == [2]*(n):
                return 2
                break
            else:
                pass
        #horizonally 
        for i in range(0,n):
            if board[(n*i):(n*i)+n] == [1]*(n):
                return 1
            else:
                pass
        #vertically
        for i in range(0, n):
            if board[i:(n*(n-1))+(i+1):n] == [1]*(n):
                return 1
            else:
                pass
        #diagonally
        for i in range(0, n**2, n+1):
            if board[0::n+1] == [1]*(n):
                return 1
                break
            else:
                pass
        for i in range(0, n*(n-1)+1, n-1):
            if board[n-1:(n*n)-(n-1):(n-1)] == [1]*(n):
                return 1
                break
            else:
                pass
        else:
            return 0
    elif who_played == 2:
        #horizonally 
        for i in range(0,n):
            if board[(n*i):(n*i)+n] == [1]*(n):
                return 1
            else:
                pass
        #vertically
        for i in range(0, n):
            if board[i:(n*(n-1))+(i+1):n] == [1]*(n):
                return 1
            else:
                pass
        #diagonally
        for i in range(0, n**2, n+1):
            if board[0::n+1] == [1]*(n):
                return 1
                break
            else:
                pass
        for i in range(0, n*(n-1)+1, n-1):
            if board[n-1:(n*n)-(n-1):(n-1)] == [1]*(n):
                return 1
                break
            else:
                pass
        #horizonally 
        for i in range(0,n):
            if board[n*i:n*i+n] == [2]*(n):
                return 2
            
        #vertically
        for i in range(0, n):
            if board[i:(n*(n-1))+(i+1):n] == [2]*(n):
                return 2
            else:
                pass
        #diagonally
        if board[0::n+1] == [2]*(n):
            return 2
        elif board[n-1:(n*n)-(n-1):(n-1)] == [2]*(n):
            return 2
        else:
            return 0
          

def computer_move(board, turn, level):
    n = int(math.sqrt(len(board)))
    list1 = []
    for i in range (0, n**2):
        if 0 <= i <= n-1:
            list1.append(i)
        elif i%n == 0:
            list1.append(i)
        elif (i+1)%n == 0:
            list1.append(i)
        elif n*(n-1) <= i <= (n**2)-1:
            list1.append(i)
    direction = ['T', 'B', 'L', 'R']
    d1 = ['L', 'R', 'B']
    d2 = ['L', 'B', 'T']
    d3 = ['R', 'B', 'T']
    d4 = ['L', 'R', 'T']
    d5 = ['R', 'B']
    d6 = ['L', 'B']
    d7 = ['R', 'T']
    d8 = ['L', 'T']
    list2 = []
    for i in range (0, n**2):
        if 1 <= i <= n-2:
            for d in d1:
                list2.append((i, d))
        elif n*(n-1)+1 <= i <= (n**2)-2:
            for d in d4:
                list2.append((i, d))
    for i in range (n, n*(n-1) -1, n):
        for d in d3:
            list2.append((i,d))
    for i in range (n*2 -1, n*(n-1), n):
        for d in d2:
            list2.append((i,d))
    for d in d5:
        list2.append((0, d))
    for d in d6:
        list2.append((n-1, d))
    for d in d7:
        list2.append((n*(n-1), d))
    for d in d8:
        list2.append((n**2-1, d))
    

    if level == 1: #random choice of move from computer     
        # Assumes turn = 2
        correct_move = 0
        while correct_move == 0:
            index = random.choice(list1)
            directionchoice = random.choice(direction)
            if check_move(board, 2, index, directionchoice) is True:
                correct_move += 1        
    elif level == 2:
        # Assumes computer turn = 2
        ryan = list2[:]
        tester = board[:]
        aldan = list2[:]
        #kill = [2]*(n)
        #slam = [1]*(n)
        #case 1: comp direct win
        for i in ryan:
            if check_move(tester, 2, i[0], i[1]) is True:
                tester = board[:]
                tester = apply_move(tester, 2, i[0], i[1])
                #print('kuku1')
                if check_victory(tester, 2) == 2:
                    return i
                            
        #case 2: comp direct lose (player makes a win)
        for i in ryan:
            if check_move(tester, 2, i[0], i[1]) is True:
                tester = board[:]
                tester = apply_move(tester, 2, i[0], i[1])
                if check_victory(tester, 2) == 1:
                    if i in ryan:
                        ryan.remove(i)
                        
        #case 3: don't make a move for the human to make a winning move next
        for i in ryan:
            for k in aldan:
                if check_move(tester, 2, i[0], i[1]) is True:
                    tester = board[:]
                    tester = apply_move(tester, 2, i[0], i[1]) #computer moves
                    if check_move(tester, 1, k[0], k[1]) is True:
                        tester = apply_move(tester, 1, k[0], k[1]) #human move
                        if check_victory(tester, 1) == 1:
                            if i in ryan:
                                ryan.remove(i)
                            else:
                                pass
                        else:
                            pass
        #case 4: random move
        else:
            correct_move = 0
            while correct_move == 0:
                chosenmove = random.choice(list2)
                if check_move(board, 2, chosenmove[0], chosenmove[1]) is True:
                    correct_move += 1          
            return (chosenmove[0], chosenmove[1])  
 

def display_board(board): #displays board as 5x5 Numpy array
    n = int(math.sqrt(len(board)))
    board2 = np.array(board)
    board3 = board2.reshape([n,n])
    return board3 

               
def menu():
    #global n # Ensures that value of n can be used in all other functions
    
    n = int(input('What size of board do you wish to play on? (input an integer): '))
    while n < 3 or n > 10:
        n = int(input('What board size would you like to play? (note: size of board should minimally be 3 or maximally 10) '))
    board = [0]*(n**2)
    comHuman = input("Please enter the following letters for the opponent you're playing against (H for human, C for computer): ")
    if comHuman in ('H', 'h'):
        win = 0
        valid_move = 0
        print('The player who starts first will be Player 1 (indicated as 1 on the board).')
        while win == 0: # Loops until win condition is met
            while valid_move == 0: # Loops until a valid move is chosen for player 2
                turn = 1
                print('It\'s Player 1\'s turn')
                index = int(input('Which block do you want to move? (Please enter the integer index position of the block) '))
                while index > (n**2)-1:
                    print("Index cannot be choosen! Please pick a number from 0 to", n*n-1)
                    index = int(input('Which block do you want to move? (Please enter the integer index position of the block)'))
                push_from = input('What direction would you like to push the block from? (note: choose either T, B, L, R) ').upper()
                while check_move(board, turn, index, push_from) is False: #wrong move is made, make a new move
                    print('Move cannot be made! Please choose another move.')
                    index = int(input('Which block do you want to move? (Please enter the integer index position of the block) '))
                    while index > (n**2)-1:
                        print("Index cannot be choosen! Please pick a number from 0 to", n*n-1)
                        index = int(input('Which block do you want to move? (Please enter the integer index position of the block)'))
                    push_from = input('What direction would you like to push the block from? (note: choose either T, B, L, R) ').upper()
                if check_move(board, turn, index, push_from) is True: # If move is valid, apply the move and check if anyone won
                    board = apply_move(board, turn, index, push_from)
                    print(display_board(board))
                    valid_move += 1
            
                    if check_victory(board, turn) == 1:
                        win += 1
                        valid_move = 5
                        print('Congratulations Player 1, you won!')
                        print(display_board(board)) 
                        playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                        if playagain == 'YES':
                            menu()
                        elif playagain == 'NO':
                            break
                
                    elif check_victory(board, turn) == 2:
                        win += 1
                        valid_move = 5
                        print('Congratulations Player 2, you won!')
                        print(display_board(board))  
                        playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                        if playagain == 'YES':
                            menu()
                        elif playagain == 'NO':
                            break
                        
            while valid_move == 1: # Loops until a valid move is chosen for Player 2
                turn = 2
                print('It\'s Player 2\'s turn')
                index = int(input('Which block do you want to move? (Please enter the integer index position of the block) '))
                while index > (n**2)-1:
                    print("Index cannot be choosen! Please pick a number from 0 to", n*n-1)
                    index = int(input('Which block do you want to move? (Please enter the integer index position of the block)'))
                push_from = input('What direction would you like to push the block from? (note: choose either T, B, L, R) ').upper()
                while check_move(board, turn, index, push_from) is False: #wrong move is made, make a new move
                    print('Move cannot be made! Please choose another move.')
                    index = int(input('Which block do you want to move? (Please enter the integer index position of the block) '))
                    while index > (n**2)-1:
                        print("Index cannot be choosen! Please pick a number from 0 to", n*n-1)
                        index = int(input('Which block do you want to move? (Please enter the integer index position of the block)'))
                    push_from = input('What direction would you like to push the block from? (note: choose either T, B, L, R) ').upper()
                    
                if check_move(board, turn, index, push_from) is True: # If move valid, play the move and check if anyone won
                    board = apply_move(board, turn, index, push_from)
                    print(display_board(board))
                    valid_move -= 1
            
                    if check_victory(board, turn) == 1:
                        win += 1
                        valid_move = 5
                        print('Congratulations Player 1, you won!')
                        print(display_board(board))
                        playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                        if playagain == 'YES':
                            menu()
                        elif playagain == 'NO':
                            break
                                          
                
                    elif check_victory(board, turn) == 2:
                        win += 1
                        valid_move = 5
                        print('Congratulations Player 2, you won!')
                        print(display_board(board)) 
                        playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                        if playagain == 'YES':
                            menu()
                        elif playagain == 'NO':
                            break
                    
    elif comHuman in ('C', 'c'):
        win = 0
        valid_move = 0
        level = int(input('What difficulty would you like to play? (1 for easy, 2 for medium): '))
        print('Note that you are Player 1, and your piece is indicated as 1. ')
        if level == 1:
            while win == 0: # Loops until win condition is met
                while valid_move == 0: # Loops until a valid move is chosen for human player
                    turn = 1
                    print('It\'s your turn.')
                    index = int(input('Which block do you want to move? (Please enter the integer index position of the block) '))
                    while index > (n**2)-1:
                        print("Index cannot be choosen! Please pick a number from 0 to", n*n-1)
                        index = int(input('Which block do you want to move? (Please enter the integer index position of the block)'))
                    push_from = input('What direction would you like to push the block from? (note: choose either T, B, L, R) ').upper()
                    while check_move(board, turn, index, push_from) is False: #wrong move is made, make a new move
                        print('Move cannot be made! Please choose another move.')
                        index = int(input('Which block do you want to move? (Please enter the integer index position of the block) '))
                        while index > (n**2)-1:
                            print("Index cannot be choosen! Please pick a number from 0 to", n*n-1)
                            index = int(input('Which block do you want to move? (Please enter the integer index position of the block)'))
                        push_from = input('What direction would you like to push the block from? (note: choose either T, B, L, R) ').upper()
                        
                    if check_move(board, turn, index, push_from) is True: # If move is valid, apply the move and check if anyone won
                        board = apply_move(board, turn, index, push_from)
                        print(display_board(board))
                        valid_move += 1
                        
                        if check_victory(board, turn) == 1:
                            win += 1
                            valid_move = 5
                            print('Congratulations, you\'ve won!')
                            print(display_board(board)) 
                            playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                            if playagain == 'YES':
                                menu()
                            elif playagain == 'NO':
                                break
                            
                    
                        elif check_victory(board, turn) == 2:
                            win += 1
                            valid_move = 5
                            print('The computer has won...')
                            print(display_board(board))
                            playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                            if playagain == 'YES':
                                menu()
                            elif playagain == 'NO':
                                break
                    
                # COMPUTER PLAYER
                        turn = 2
                        a = computer_move(board, turn, 1) #Turn 2, level 1. Returns tuple of block chosen and direction of push
                        board = apply_move(board, turn, a[0], a[1])
                        print('____________')
                        print('The computer moved (index, push direction) of ' + str(a))
                        print(display_board(board))
                    
                        if check_victory(board, 2) == 1:
                            win += 1
                            valid_move = 5
                            print('The computer has made a wrong move you won!')
                            print(display_board(board))  
                            playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                            if playagain == 'YES':
                                menu()
                            elif playagain == 'NO':
                                break
                    
                        elif check_victory(board, 2) == 2:
                            win += 1
                            valid_move = 5
                            print('The computer has won..')
                            print(display_board(board))
                            playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                            if playagain == 'YES':
                                menu()
                            elif playagain == 'NO':
                                break
                        
                        else: # Rerun loop if nobody has won after the computer's move
                            valid_move = 0 
                            
        elif level == 2:
            while win == 0: # Loops until win condition is met
                while valid_move == 0: # Loops until a valid move is chosen for human player
                    turn = 1
                    print('It\'s your turn.')
                    index = int(input('Which block do you want to move? (Please enter the integer index position of the block) '))
                    while index > (n**2)-1:
                        print("Index cannot be choosen! Please pick a number from 0 to", n*n-1)
                        index = int(input('Which block do you want to move? (Please enter the integer index position of the block)'))
                    push_from = input('What direction would you like to push the block from? (note: choose either T, B, L, R) ').upper()
                    while check_move(board, turn, index, push_from) is False: #wrong move is made, make a new move
                        print('Move cannot be made! Please choose another move.')
                        index = int(input('Which block do you want to move? (Please enter the integer index position of the block) '))
                        while index > (n**2)-1:
                            print("Index cannot be choosen! Please pick a number from 0 to", n*n-1)
                            index = int(input('Which block do you want to move? (Please enter the integer index position of the block)'))
                        push_from = input('What direction would you like to push the block from? (note: choose either T, B, L, R) ').upper()
                    
                    if check_move(board, turn, index, push_from) is True: # If move is valid, apply the move and check if anyone won
                        board = apply_move(board, turn, index, push_from)
                        print(display_board(board))
                        valid_move += 1
                
                        if check_victory(board, turn) == 1:
                            win += 1
                            valid_move = 5
                            print('Congratulations, you\'ve won!')
                            print(display_board(board)) 
                            playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                            if playagain == 'YES':
                                menu()
                            elif playagain == 'NO':
                                break
                    
                        elif check_victory(board, turn) == 2:
                            win += 1
                            valid_move = 5
                            print('The computer has won...')
                            print(display_board(board))
                            playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                            if playagain == 'YES':
                                menu()
                            elif playagain == 'NO':
                                break

                # COMPUTER PLAYER
                        turn = 2
                        a = computer_move(board, turn, 2) #Turn 2, level 2. Returns tuple of block chosen and direction of push
                        board = apply_move(board, turn, a[0], a[1])
                        print('____________')
                        print('The computer moved (index, push direction) of ' + str(a))
                        print(display_board(board))
                        
                    
                        if check_victory(board, 2) == 1:
                            win += 1
                            valid_move = 5
                            print('The computer has made a wrong move you won!')
                            print(display_board(board))  
                            playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                            if playagain == 'YES':
                                menu()
                            elif playagain == 'NO':
                                break
                    
                        elif check_victory(board, 2) == 2:
                            win += 1
                            valid_move = 5
                            print('The computer has won..')
                            print(display_board(board))
                            playagain = input("Would you like to play again? (Please enter yes or no) ").upper()
                            if playagain == 'YES':
                                menu()
                            elif playagain == 'NO':
                                break
                        
                        else: # Rerun loop if nobody has won after the computer's move
                            valid_move = 0
                              

if __name__ == "__main__":
    menu()








