import random
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
import requests
import socket
 #màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
lam = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
logo = f"""
    Ấn ENTER ĐỂ VÀO TRÒ CHƠI
    """
Anime.Fade(Center.Center(logo), Colors.red_to_yellow, Colorate.Vertical, enter=True)
p = 0
while p<=9:
    p= p + 1
    print(f'{do}[  {vang}Đang Kết Nối {do}]{do}[{lam}|{do}]{tim}[LO......][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[ {xam} Đang Kết Nối {do}]{do}[{black}/{do}]{luc}[LOA.....][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[ {hong} Đang Kết Nối {do}]{do}[{tim}-{do}]{vang}[LOAD....][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[  {luc}Đang Kết Nối{do}]{do}[{luc}+{do}]{xduong}[LOADI...][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[  {lam}Đang Kết Nối {do}]{do}[{xam}\{do}]{trang}[LOADIN..][{p}]','     ',end='\r');sleep(1/6)
    print(f'{do}[  {trang}Đang Kết Nối {do}][{xduong}|{do}]{xam}[LOADING.][{p}]','     ',end='\r');sleep(1/6)
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner=f"""
            \033[1;36m╭─⋞─────────────────────────────────────────────────────╮
            \033[1;31m███╗   ██╗ █████╗ ███╗   ███╗    ██████  ███████╗██╗   ██╗          
            \033[1;32m████╗  ██║██╔══██╗████╗ ████║    ██╔══██╗██╔════╝██║   ██║          
            \033[1;33m██╔██╗ ██║███████║██╔████╔██║    ██║  ██║█████╗  ╚██╗ ██╔╝          
            \033[1;34m██║╚██╗██║██╔══██║██║╚██╔╝██║    ██║  ██║██╔══╝   ╚████╔╝           
            \033[1;35m██║ ╚████║██║  ██║██║ ╚═╝ ██║    ██████╔╝███████╗  ╚██╔╝            
            \033[1;36m╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   
            \033[1;34m Youtube : \033[1;37mhttps://youtube.com/@NamTool1
            \033[1;34m Nhóm Zalo : \033[1;37mhttps://zalo.me/g/kfmgqm225
            \033[1;34m Facebook   : \033[1;37mhttps://facebook.com/nam.nhn131 
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯ 
            \033[1;31m                      TIC-TAC-TOE
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
 """
    print(banner)
banner()   
def drawBoard(board):
    #Thực hiện in ra bàn cờ
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
 
def inputPlayerLetter():
    #Cho phép người chơi nhập ký tự mà họ muốn sử dụng
    #Trả về tập hợp kiểu List với ký tự mà người chơi chọn làm phần tử đầu tiên
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(f'{trang}Bạn muốn chọn X hay O?')
        letter = input().upper()
 
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def whoGoesFirst():
    #Chọn ngẫu nhiên bất kỳ cho phép người chơi đi trước hay không
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
 
def makeMove(board, letter, move):
    board[move] = letter
 
def isWinner(bo, le):
    #Trả về True nếu người chơi thắng
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))
 
def getBoardCopy(board):
    #Sao chép bàn cờ
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
 
def isSpaceFree(board, move):
    #Trả về True nếu nước đi còn chỗ trống
    return board[move] == ' '
 
def getPlayerMove(board):
    #Lấy nước đi của người chơi
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Nước đi của bạn? (1-9)')
        move = input()
    return int(move)
 
def chooseRandomMoveFromList(board, movesList):
    #Trả về một nước đi hợp lệ
    #Trả về None nếu không còn nước đi hợp lệ
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
 
def getComputerMove(board, computerLetter):
    #Xác định nước đi cho máy
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 
    #Giải thuật cho máy chơi
    #Kiểm tra xem nước đi tiếp theo có thắng được hay không
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
 
    #Kiểm tra xem người chơi có thể thắng trong nước đi tiếp theo hay không
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
 
    #Chọn một nước đi ở các góc bàn cờ nếu trống
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
 
    #Chọn nước đi ở giữa
    if isSpaceFree(board, 5):
        return 5
 
    #Chọn một trong các nước đi ở các cạnh bên của bàn cờ
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
 
def isBoardFull(board):
    #Trả về True nếu các nước đi không còn, ngược lại trả về False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
    print(f'{vang}Chào mừng đến Tic-Tac-Toe!')

while True:
    #Thiết lập lại bàn cờ
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
 
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
 
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print(f'{luc}Hooray! Bạn đã thắng!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print(f'{lam}Bạn và máy hòa!')
                    break
                else:
                    turn = 'computer'
 
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
 
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print(f'{do}Máy đã thắng. Cố gắng lượt sau nhé!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print(f'{lam}Bạn và máy hòa!')
                    break
                else:
                    turn = 'player'
    print(f'{trang}Bạn muốn chơi lại không?')
    print(f'{vang}Ấn (Enter) để thoát (Y) để chơi tiếp')
    if not input().lower().startswith('y'):
        break