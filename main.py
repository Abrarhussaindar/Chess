board = [
    ['B_L_E', 'B_L_H', 'B_L_C', 'B_Q', 'B_K', 'B_R_C', 'B_R_H', 'B_R_E'],
    [' B_S ', ' B_S ', ' B_S ', 'B_S', 'B_S', ' B_S ', ' B_S ', ' B_S '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' W_S ', ' W_S ', ' W_S ', 'W_S', 'W_S', ' W_S ', ' W_S ', ' W_S '],
    ['W_L_E', 'W_L_H', 'W_L_C', 'W_Q', 'W_K', 'W_R_C', 'W_R_H', 'W_R_E']
]
def print_board():
    print("\nChess Board:\n")
    for row in board:
        print(row)
print_board()


def Indicies():
    print("\nIndicies for the board:\n")
    indicies = [
        ['00', '01', '02', '03', '04', '05', '06', '07'],
        ['10', '11', '12', '13', '14', '15', '16', '17'],
        ['20', '21', '22', '23', '24', '25', '26', '27'],
        ['30', '31', '32', '33', '34', '35', '36', '37'],
        ['40', '41', '42', '43', '44', '45', '46', '47'],
        ['50', '51', '52', '53', '54', '55', '56', '57'],
        ['60', '61', '62', '63', '64', '65', '66', '67'],
        ['70', '71', '72', '73', '74', '75', '76', '77']
    ]
    return indicies
class Pieces():
    def __init__(self, name: str, ist_index: int, second_index: int):
        self.name = name
        self.ist_index = ist_index
        self.second_index = second_index
    
    def __str__(self) -> str:
        self.name


# e1 = Enimy_pieces("B_L_E", 0, 0)
Black_piece_list = []
Black_piece_list.append(Pieces("B_L_E", 0, 0))
Black_piece_list.append(Pieces("B_L_H", 0, 1))
Black_piece_list.append(Pieces("B_L_C", 0, 2))
Black_piece_list.append(Pieces("B_Q", 0, 3))
Black_piece_list.append(Pieces("B_K", 0, 4))
Black_piece_list.append(Pieces("B_R_C", 0, 5))
Black_piece_list.append(Pieces("B_R_H", 0, 6))
Black_piece_list.append(Pieces("B_R_E", 0, 7))
Black_piece_list.append(Pieces("B_S", 1, 0))

# for obj in Black_piece_list:
#     print(obj.name)
#     if obj.name == "B_L_E":
#         print(obj.ist_index, obj.second_index)

print("\n")

White_piece_list = []
White_piece_list.append(Pieces("W_L_E", 7, 0))
White_piece_list.append(Pieces("W_L_H", 7, 1))
White_piece_list.append(Pieces("W_L_C", 7, 2))
White_piece_list.append(Pieces("W_Q", 7, 3))
White_piece_list.append(Pieces("W_K", 7, 4))
White_piece_list.append(Pieces("W_R_C", 7, 5))
White_piece_list.append(Pieces("W_R_H", 7, 6))
White_piece_list.append(Pieces("W_R_E", 7, 7))
White_piece_list.append(Pieces("W_S", 6, 0))

# for obj in White_piece_list:
#     print(obj.name)

# print(e1.name)
# print()
black_enemy_pieces = ["B_L_E", "B_L_H", "B_L_C", "B_Q", "B_K", "B_R_C", "B_R_H", "B_R_E", "B_S"]
white_enemy_pieces = ["W_L_E", "W_L_H", "W_L_C", "W_Q", "W_K", "W_R_C", "W_R_H", "W_R_E", "W_S"]

# def adj_piece_king(piece, r,i):
#     for c in range(0,8):
#         if board[row][]



def check_adj_enemy_pieces(ene):
    # print("in caep: ", ene)
    # print(len(enemy_pieces))
    for i in range(0, len(black_enemy_pieces)):
        
        if black_enemy_pieces[i] == ene:
            # print("for ene",enemy_pieces[i])
            # print("true")
            return True
        #     # pass
def check_adj_same_pieces(ene, which_fun):
    print("in ", which_fun, "if fun", ene)
    for i in range(0, len(white_enemy_pieces)):
        print("in", which_fun, "for fun", ene)
        if ene == white_enemy_pieces[i]:
            print("in ", which_fun, " for i =", i, " if fun", ene)
            print("for ene",white_enemy_pieces[i])
            print("true")
            return True
        # else:
        #     return False
    # r = 7
    # c = 4

    # # right
    # c =+1
    # for c in range(c, 8):
    #     for i in range(0,len(white_enemy_pieces)):
    #         if board[r][c] == white_enemy_pieces[i]:
    #             print("piece at ", board[r][c+1], "white_piece ", white_enemy_pieces[i])
    #             return True
    # # left

    # while(c>0):
    #     for i in range(0,len(white_enemy_pieces)):
    #         if board[r][c] == white_enemy_pieces[i]:
    #             print("piece at ", board[r][c], "white_piece ", white_enemy_pieces[i])
    #             return True
    #     c=-1

    # # upwards

    # while(r>0):
    #     for i in range(0,len(white_enemy_pieces)):
    #         if board[r][col] == white_enemy_pieces[i]:
    #             print("piece at ", board[r][col], "white_piece ", white_enemy_pieces[i])
    #             return True
    #     r=-1

    # # downwards 
    # while(r<8):
    #     for i in range(0,len(white_enemy_pieces)):
    #         if board[r][col] == white_enemy_pieces[i]:
    #             print("piece at ", board[r][col], "white_piece ", white_enemy_pieces[i])
    #             return True
    #     r=+1
    # right upper diagonal
    

    # for i in range(0, len(white_enemy_pieces)):
    #     if white_enemy_pieces[i] == ene:
    #         return True
        # print
# def check_adjecent_piece(piece):
#     count = 0
#     for adj_piece in board:
#         # print(adj_piece[0])
#         # while(count<=8):
#         if adj_piece[count] == piece:
#             print("at count " + str(count) + " true")
#             count = count + 1
#             print(count)
        # count = 0
        # for i in range(8):
        #     count = count +1
            # while("W_K" != adj_piece[i]):
            # if piece == adj_piece[i]:
                
            #     print(" count: " + str(count) + " " + adj_piece[i])
            #     # if check_enemy_pieces(adj_piece) == True:
            #     #     return adj_piece
            # else:
            #     break
# list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# piece = "B_L_E"
# r = 0
# second_index = 0
# col_boundry = (8 - second_index)
# col = second_index
# for col in range(col_boundry):
#     # print(col)
#     print(board[r][col])
#     if piece == check_adjecent_piece(board[r][col]):
#         print("enimy found")

# ist_index = 0
# c = 0
# row_boundry = (8- ist_index)
# for row in range(row_boundry):
#     if piece == check_adjecent_piece(board[row][c]):
#         print("enimy found")
def B_L_E_fun(row,col):
    if row == col == 0:
        for i in range(0,8):
            if check_adj_enemy_pieces(board[row][i]):
                pass
            else:
                if board[row][i] == "W_K":
                    print("check mate") 

def B_L_H_fun(row,col):
    pass

def B_L_C_fun(row,col):
    pass

def B_Q_fun(row,col):
    pass

def B_K_fun(row,col):
    pass

def B_R_C_fun(row,col):
    pass

def B_R_H_fun(row,col):
    pass

def B_R_E_fun(row,col):
    pass



    # if board[row][col] == "B_L_E":
    #     B_L_E_fun(row,col)
    # if board[row][col] == "B_L_H":
    #     B_L_H_fun(row, col)
    # if board[row][col] == "B_L_C":
    #     B_L_C_fun(row, col)
    # if board[row][col] == "B_Q":
    #     B_Q_fun(row, col)
    # if board[row][col] == "B_K":
    #     B_K_fun(row, col)
    # if board[row][col] == "B_R_C":
    #     B_R_C_fun(row, col)
    # if board[row][col] == "B_R_H":
    #     B_R_H_fun(row, col)
    # if board[row][col] == "B_R_E":
    #     B_R_E_fun(row, col)
#     i=7
#     j=4
#     for row in range(0,8):
#         for col in range(0,8):
#             if check_enemy_pieces() == board[row][col]:
                # check_adjecent_piece() ==  

def print_indicies():
    indicies = Indicies()
    for row in indicies:
        print(row)
# print_indicies()
# steps_for_K = 1
# steps_for_Q = 10
# steps_for_M = 10
# steps_for_H = 3
# steps_for_E = 10
# steps_for_S = 1

# print()
# def piece_to_be_moved():

def input_piece():
    piece = str(input("\nEnter the chess piece in capital only which u want to move: \n"))
# print("here: ", piece)
    return piece
# input_piece()

def input_indicies():
    index_from_1 = int(input("\nEnter the ist index of that chess piece which you want to move: ")) 
    index_from_2 = int(input("\nEnter the 2nd index of that chess piece which you want to move: "))
            

    index_to_1 = int(input("\nEnter the ist index where you want to move your chess piece: ")) 
    index_to_2 = int(input("\nEnter the 2nd index where you want to move your chess piece: "))
    board[index_to_1][index_to_2] = board[index_from_1][index_from_2]

    if index_from_1 == 7 and index_from_2 == 4:
        if board[index_from_1][index_from_2] == "W_K":
            king_row = index_to_1
            king_col = index_to_2
    # print("row:", king_row, "col", king_col)

    if(index_to_2 < 3 or index_to_2 > 4):
        board[index_from_1][index_from_2] = ' - '
    else:
        board[index_from_1][index_from_2] = '-'
    CheckMate(king_row, king_col)

    # return index_1, index_2

def traveling_right(row, col):
    str = "right"
    for c in range(col+1,8):
        # print("col",c)
        
        ene = board[row][c]
        print("in right", ene)
        if check_adj_same_pieces(ene, str):
            print("in right if", ene)
            print("its present their at adj positons in right fun")
            break
        elif check_adj_enemy_pieces(ene):
            print(" enemy found true its present their at adj positons")
            if ene == "B_L_E":
                print("true its here")
                print("checkmate")
                B_L_E_fun(row,col)
            if ene == "B_L_H":
                B_L_H_fun(row, col)
            if ene == "B_L_C":
                B_L_C_fun(row, col)
            if ene == "B_Q":
                print("true its here")
                print("checkmate")
                B_Q_fun(row, col)
            if ene == "B_K":
                B_K_fun(row, col)
            if ene == "B_R_C":
                print("true its here")
                # B_R_C_fun(row, col)
                pass
            if ene == "B_R_H":
                # B_R_H_fun(row, col)
                print("true its here")
            if ene == "B_R_E":
                print("true its here")
                print("checkmate")
                B_R_E_fun(row, col)

def traveling_right_upper_diagonal(row, col):
    r = row
    c = col
    # while(r>=0):
    # for r in range(row-1,row-row):
    # for c in range(col+1,8):
    while(r>=0 or c<=7):
        # print("piece in rud ", board[r][c], " r=",r, " c=",c)

        ene = board[r-1][c+1]
        str = "rud"
        print("ene ",ene, "at r=", r-1, " and c=", c+1)
        if check_adj_same_pieces(ene, str):
            print("its present their at adj positons in rud")
            break
        elif check_adj_enemy_pieces(ene):
            print(" enemy found true")
            if ene == "B_L_E":
                print("true its here")
                print("checkmate")
                B_L_E_fun(row,col)
            if ene == "B_L_H":
                B_L_H_fun(row, col)
            if ene == "B_L_C":
                print("true its here")
                print("checkmate")
                B_L_C_fun(row, col)
            if ene == "B_Q":
                print("true its here")
                print("checkmate")
                B_Q_fun(row, col)
            if ene == "B_K":
                B_K_fun(row, col)
            if ene == "B_R_C":
                print("true its here")
                print("checkmate")
                # B_R_C_fun(row, col)
                pass
            if ene == "B_R_H":
                # B_R_H_fun(row, col)
                print("true its here")
            if ene == "B_R_E":
                print("true its here")
                print("checkmate")
                B_R_E_fun(row, col)

        r= r-1
        c=c+1

def traveling_right_lower_diagonal(row, col):
    r = row
    c = col
    # print("r",r  ,"c",c)
    while(r<8 and c<8):
        # print("piece in lrd", board[r][c], " r=",r, " c=",c)

        ene = board[r][c]
        str = "rld"
        if check_adj_same_pieces(ene, str):
            print("its present their at adj positons in rld")
            break
        elif check_adj_enemy_pieces(ene):
            print(" enemy found true")
            if ene == "B_L_E":
                print("true its here")
                print("checkmate")
                B_L_E_fun(row,col)
            if ene == "B_L_H":
                B_L_H_fun(row, col)
            if ene == "B_L_C":
                print("true its here")
                print("checkmate")
                B_L_C_fun(row, col)
            if ene == "B_Q":
                print("true its here")
                print("checkmate")
                B_Q_fun(row, col)
            if ene == "B_K":
                B_K_fun(row, col)
            if ene == "B_R_C":
                print("true its here")
                                # print("true its here")
                print("checkmate")
                # B_R_C_fun(row, col)
                pass
            if ene == "B_R_H":
                # B_R_H_fun(row, col)
                print("true its here")
            if ene == "B_R_E":
                print("true its here")
                print("checkmate")
                B_R_E_fun(row, col)     

        r= r+1
        c=c+1

def traveling_left(row, col):
    c = col
    print("c in left", c)
    print("row in left",row)

    # traveling to left
    while (c>=0):
        # print("col", c)
        ene = board[row][c-1]
        str = "left"
        if check_adj_same_pieces(ene, str):
            print("its present their at adj positons in left")
            break
        elif check_adj_enemy_pieces(ene):
            print(" enemy found true")
            if ene == "B_L_E":
                print("true its here")
                print("checkmate")
                B_L_E_fun(row,col)
            if ene == "B_L_H":
                B_L_H_fun(row, col)
            if ene == "B_L_C":
                B_L_C_fun(row, col)
            if ene == "B_Q":
                print("true its here")
                print("checkmate")
                B_Q_fun(row, col)
            if ene == "B_K":
                B_K_fun(row, col)
            if ene == "B_R_C":
                print("true its here")
                # B_R_C_fun(row, col)
                pass
            if ene == "B_R_H":
                # B_R_H_fun(row, col)
                print("true its here")
            if ene == "B_R_E":
                print("true its here")
                print("checkmate")
                B_R_E_fun(row, col)

        c = c-1

def traveling_left_upper_diagonal(row, col):
    r = row
    c = col
    # print("r",r  ,"c",c)
    while(r>=0 and c>=0):
        # print("piece in urd", board[r][c], " r=",r, " c=",c)

        ene = board[r][c]
        str = "lud"
        if check_adj_same_pieces(ene, str):
            print("its present their at adj positons lud")
            break
        elif check_adj_enemy_pieces(ene):
            print(" enemy found true")
            if ene == "B_L_E":
                print("true its here")
                print("checkmate")
                B_L_E_fun(row,col)
            if ene == "B_L_H":
                B_L_H_fun(row, col)
            if ene == "B_L_C":
                print("true its here")
                print("checkmate")
                B_L_C_fun(row, col)
            if ene == "B_Q":
                print("true its here")
                print("checkmate")
                B_Q_fun(row, col)
            if ene == "B_K":
                B_K_fun(row, col)
            if ene == "B_R_C":
                print("true its here")
                                # print("true its here")
                print("checkmate")
                # B_R_C_fun(row, col)
                pass
            if ene == "B_R_H":
                # B_R_H_fun(row, col)
                print("true its here")
            if ene == "B_R_E":
                print("true its here")
                print("checkmate")
                B_R_E_fun(row, col)

        r= r-1
        c=c-1

def traveling_left_lower_diagonal(row, col):
    r = row
    c = col
    # print("r",r  ,"c",c)
    while(r<8 and c>=0):
        # print("piece in lld", board[r][c], " r=",r, " c=",c)

        ene = board[r][c]
        str = "lld"
        if check_adj_same_pieces(ene, str):
            print("its present their at adj positons in lld")
            break
        elif check_adj_enemy_pieces(ene):
            print(" enemy found true")
            if ene == "B_L_E":
                print("true its here")
                print("checkmate")
                B_L_E_fun(row,col)
            if ene == "B_L_H":
                B_L_H_fun(row, col)
            if ene == "B_L_C":
                print("true its here")
                print("checkmate")
                B_L_C_fun(row, col)
            if ene == "B_Q":
                print("true its here")
                print("checkmate")
                B_Q_fun(row, col)
            if ene == "B_K":
                B_K_fun(row, col)
            if ene == "B_R_C":
                print("true its here")
                                # print("true its here")
                print("checkmate")
                # B_R_C_fun(row, col)
                pass
            if ene == "B_R_H":
                # B_R_H_fun(row, col)
                print("true its here")
            if ene == "B_R_E":
                print("true its here")
                print("checkmate")
                B_R_E_fun(row, col)

            

        r= r+1
        c=c-1

def traveling_upwards(row, col):
    r = row
    while (r>=0):
        # print("row", r)
        ene = board[r-1][col]
        str = "up"
        if check_adj_same_pieces(ene, str):
            print("its present their at adj positons in up")
            break
        elif check_adj_enemy_pieces(ene):
            print(" enemy found true")
            if ene == "B_L_E":
                print("true its here")
                print("checkmate")
                B_L_E_fun(row,col)
            if ene == "B_L_H":
                B_L_H_fun(row, col)
            if ene == "B_L_C":
                B_L_C_fun(row, col)
            if ene == "B_Q":
                print("true its here")
                print("checkmate")
                B_Q_fun(row, col)
            if ene == "B_K":
                B_K_fun(row, col)
            if ene == "B_R_C":
                print("true its here")
                # B_R_C_fun(row, col)
                pass
            if ene == "B_R_H":
                # B_R_H_fun(row, col)
                print("true its here")
            if ene == "B_R_E":
                print("true its here")
                print("checkmate")
                B_R_E_fun(row, col)
        r = r-1

def traveling_downwards(row, col):
    for r in range(row+1, 8):
        # print("row in downwards",r)
        ene = board[r][col]
        str = "down"
        if check_adj_same_pieces(ene, str):
            print("its present their at adj positons in down")
            break
        elif check_adj_enemy_pieces(ene):
            print(" enemy found true")
            if ene == "B_L_E":
                print("true its here")
                print("checkmate")
                B_L_E_fun(row,col)
            if ene == "B_L_H":
                B_L_H_fun(row, col)
            if ene == "B_L_C":
                B_L_C_fun(row, col)
            if ene == "B_Q":
                print("true its here")
                print("checkmate")
                B_Q_fun(row, col)
            if ene == "B_K":
                B_K_fun(row, col)
            if ene == "B_R_C":
                print("true its here")
                # B_R_C_fun(row, col)
                pass
            if ene == "B_R_H":
                # B_R_H_fun(row, col)
                print("true its here")
            if ene == "B_R_E":
                print("true its here")
                print("checkmate")
                B_R_E_fun(row, col)


def CheckMate(row, col):
    # row = 7
    # col = 4
    # print("in check mate row", row, "col", col)
    if board[row][col] == "W_K":
        # print("true")

        
        # traveling to right
        # if check_adj_same_pieces(row, col):
            # print("true")
            # pass
            # print("piece", board[row][col+1])
        # else:
        traveling_right(row, col)
        # for c in range(col+1,8):
        #     # print("col",c)
        #     ene = board[row][c]
        #     # print(ene)
        #     if check_adj_enemy_pieces(ene):
        #         print(" enemy found true")
        #         if ene == "B_L_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_E_fun(row,col)
        #         if ene == "B_L_H":
        #             B_L_H_fun(row, col)
        #         if ene == "B_L_C":
        #             B_L_C_fun(row, col)
        #         if ene == "B_Q":
        #             print("true its here")
        #             print("checkmate")
        #             B_Q_fun(row, col)
        #         if ene == "B_K":
        #             B_K_fun(row, col)
        #         if ene == "B_R_C":
        #             print("true its here")
        #             # B_R_C_fun(row, col)
        #             pass
        #         if ene == "B_R_H":
        #             # B_R_H_fun(row, col)
        #             print("true its here")
        #         if ene == "B_R_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_R_E_fun(row, col)

        # print("col: ",col)
        # print("row: ",row)
        # print("-------")
        # c = col
        # print("c", c)
        # print("row",row)

        # traveling to left
        # if check_adj_same_pieces(row, col):
        #     # print("true")
        #     pass
        #     # print("piece", board[row][col+1])
        # else:
        traveling_left(row, col)
        # while (c>=0):
        #     # print("col", c)
        #     ene = board[row][c]
        #     # print(ene)
        #     if check_adj_enemy_pieces(ene):
        #         print(" enemy found true")
        #         if ene == "B_L_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_E_fun(row,col)
        #         if ene == "B_L_H":
        #             B_L_H_fun(row, col)
        #         if ene == "B_L_C":
        #             B_L_C_fun(row, col)
        #         if ene == "B_Q":
        #             print("true its here")
        #             print("checkmate")
        #             B_Q_fun(row, col)
        #         if ene == "B_K":
        #             B_K_fun(row, col)
        #         if ene == "B_R_C":
        #             print("true its here")
        #             # B_R_C_fun(row, col)
        #             pass
        #         if ene == "B_R_H":
        #             # B_R_H_fun(row, col)
        #             print("true its here")
        #         if ene == "B_R_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_R_E_fun(row, col)

        #     c = c-1

        # traveling upwards
        # if check_adj_same_pieces(row, col):
        #     # print("true")
        #     pass
        #     # print("piece", board[row][col+1])
        # else: 
        traveling_upwards(row, col)
        # print("row for up", row)
        # r = row
        # while (r>=0):
        #     # print("row", r)
        #     ene = board[r][col]
        #     # print(ene)
        #     if check_adj_enemy_pieces(ene):
        #         print(" enemy found true")
        #         if ene == "B_L_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_E_fun(row,col)
        #         if ene == "B_L_H":
        #             B_L_H_fun(row, col)
        #         if ene == "B_L_C":
        #             B_L_C_fun(row, col)
        #         if ene == "B_Q":
        #             print("true its here")
        #             print("checkmate")
        #             B_Q_fun(row, col)
        #         if ene == "B_K":
        #             B_K_fun(row, col)
        #         if ene == "B_R_C":
        #             print("true its here")
        #             # B_R_C_fun(row, col)
        #             pass
        #         if ene == "B_R_H":
        #             # B_R_H_fun(row, col)
        #             print("true its here")
        #         if ene == "B_R_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_R_E_fun(row, col)
        #     r = r-1
        
        # traveling downwards
        # if check_adj_same_pieces(row, col):
        #     # print("true")
        #     pass
        #     # print("piece", board[row][col+1])
        # else: 
        traveling_downwards(row, col)
        # for r in range(row+1, 8):
        #     # print("row in downwards",r)
        #     ene = board[r][col]
        #     # print(ene)
        #     if check_adj_enemy_pieces(ene):
        #         print(" enemy found true")
        #         if ene == "B_L_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_E_fun(row,col)
        #         if ene == "B_L_H":
        #             B_L_H_fun(row, col)
        #         if ene == "B_L_C":
        #             B_L_C_fun(row, col)
        #         if ene == "B_Q":
        #             print("true its here")
        #             print("checkmate")
        #             B_Q_fun(row, col)
        #         if ene == "B_K":
        #             B_K_fun(row, col)
        #         if ene == "B_R_C":
        #             print("true its here")
        #             # B_R_C_fun(row, col)
        #             pass
        #         if ene == "B_R_H":
        #             # B_R_H_fun(row, col)
        #             print("true its here")
        #         if ene == "B_R_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_R_E_fun(row, col)


        # traveling right upper diagonal
        # if check_adj_same_pieces(row, col):
        #     pass
        # else:
        traveling_right_upper_diagonal(row, col)
        # r = row
        # c = col
        # # while(r>=0):
        # # for r in range(row-1,row-row):
        # # for c in range(col+1,8):
        # while(r>=0 and c<8):
        #     # print("piece in rud ", board[r][c], " r=",r, " c=",c)

        #     ene = board[r][c]
        #     # print(ene)
        #     if check_adj_enemy_pieces(ene):
        #         print(" enemy found true")
        #         if ene == "B_L_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_E_fun(row,col)
        #         if ene == "B_L_H":
        #             B_L_H_fun(row, col)
        #         if ene == "B_L_C":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_C_fun(row, col)
        #         if ene == "B_Q":
        #             print("true its here")
        #             print("checkmate")
        #             B_Q_fun(row, col)
        #         if ene == "B_K":
        #             B_K_fun(row, col)
        #         if ene == "B_R_C":
        #             print("true its here")
        #             print("checkmate")
        #             # B_R_C_fun(row, col)
        #             pass
        #         if ene == "B_R_H":
        #             # B_R_H_fun(row, col)
        #             print("true its here")
        #         if ene == "B_R_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_R_E_fun(row, col)

                

        #     r= r-1
        #     c=c+1
        
        # traveling lower left diagonal
        # if check_adj_same_pieces(row, col):
        #     pass
        # else:
        traveling_left_lower_diagonal(row, col)
        # r = row
        # c = col
        # # print("r",r  ,"c",c)
        # while(r<8 and c>=0):
        #     # print("piece in lld", board[r][c], " r=",r, " c=",c)

        #     ene = board[r][c]
        #     # print(ene)
        #     if check_adj_enemy_pieces(ene):
        #         print(" enemy found true")
        #         if ene == "B_L_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_E_fun(row,col)
        #         if ene == "B_L_H":
        #             B_L_H_fun(row, col)
        #         if ene == "B_L_C":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_C_fun(row, col)
        #         if ene == "B_Q":
        #             print("true its here")
        #             print("checkmate")
        #             B_Q_fun(row, col)
        #         if ene == "B_K":
        #             B_K_fun(row, col)
        #         if ene == "B_R_C":
        #             print("true its here")
        #                             # print("true its here")
        #             print("checkmate")
        #             # B_R_C_fun(row, col)
        #             pass
        #         if ene == "B_R_H":
        #             # B_R_H_fun(row, col)
        #             print("true its here")
        #         if ene == "B_R_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_R_E_fun(row, col)

                

        #     r= r+1
        #     c=c-1

        # traveling lower right diagonal
        # if check_adj_same_pieces(row, col):
        #     pass
        # else:
        traveling_right_lower_diagonal(row, col)
        # r = row
        # c = col
        # # print("r",r  ,"c",c)
        # while(r<8 and c<8):
        #     # print("piece in lrd", board[r][c], " r=",r, " c=",c)

        #     ene = board[r][c]
        #     # print(ene)
        #     if check_adj_enemy_pieces(ene):
        #         print(" enemy found true")
        #         if ene == "B_L_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_E_fun(row,col)
        #         if ene == "B_L_H":
        #             B_L_H_fun(row, col)
        #         if ene == "B_L_C":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_C_fun(row, col)
        #         if ene == "B_Q":
        #             print("true its here")
        #             print("checkmate")
        #             B_Q_fun(row, col)
        #         if ene == "B_K":
        #             B_K_fun(row, col)
        #         if ene == "B_R_C":
        #             print("true its here")
        #                             # print("true its here")
        #             print("checkmate")
        #             # B_R_C_fun(row, col)
        #             pass
        #         if ene == "B_R_H":
        #             # B_R_H_fun(row, col)
        #             print("true its here")
        #         if ene == "B_R_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_R_E_fun(row, col)     

        #     r= r+1
        #     c=c+1

        # traveling uper left diagonal
        # if check_adj_same_pieces(row, col):
        #     pass
        # else:
        traveling_left_upper_diagonal(row, col)
        # r = row
        # c = col
        # # print("r",r  ,"c",c)
        # while(r>=0 and c>=0):
        #     # print("piece in urd", board[r][c], " r=",r, " c=",c)

        #     ene = board[r][c]
        #     # print(ene)
        #     if check_adj_enemy_pieces(ene):
        #         print(" enemy found true")
        #         if ene == "B_L_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_E_fun(row,col)
        #         if ene == "B_L_H":
        #             B_L_H_fun(row, col)
        #         if ene == "B_L_C":
        #             print("true its here")
        #             print("checkmate")
        #             B_L_C_fun(row, col)
        #         if ene == "B_Q":
        #             print("true its here")
        #             print("checkmate")
        #             B_Q_fun(row, col)
        #         if ene == "B_K":
        #             B_K_fun(row, col)
        #         if ene == "B_R_C":
        #             print("true its here")
        #                             # print("true its here")
        #             print("checkmate")
        #             # B_R_C_fun(row, col)
        #             pass
        #         if ene == "B_R_H":
        #             # B_R_H_fun(row, col)
        #             print("true its here")
        #         if ene == "B_R_E":
        #             print("true its here")
        #             print("checkmate")
        #             B_R_E_fun(row, col)

        #     r= r-1
        #     c=c-1 


    else:
        # print("in black")
        ene = board[row][col]
        # print(ene)
        if check_adj_enemy_pieces(ene):
            print("true ene: ",ene)
        # print("nope")

while(True):
    # for row in range(8):
    #     for col in range(8):
    CheckMate(7, 4)
    print_indicies()
    check_adj_enemy_pieces(board[0][4])
    # input_piece()
    input_indicies()
    print_board()
# board[int(input("enter the ist index of that chess piece   "))][int(input("enter the 2nd index of that chess piece "))] = "-"
# new_board = [
#     "-----------------------------------------------------------------------------------"
#     "|",'E_L',"|", 'H_L', "|", 'M_L', "|", 'Q', "|", 'K', "|", 'M_R', "|", 'H_R', "|", 'E_R' , "|",
#     "-----------------------------------------------------------------------------------"
#     "|"' S ',"|" ' S ', "|" ' S ', "|" 'S', "|" 'S', "|" ' S ', "|" ' S',  "|" '  S ' "|",
#     "-----------------------------------------------------------------------------------"
#     "|"' - ',"|" ' - ', "|" ' - ', "|" '-', "|" '-', "|" ' - ', "|" ' -',  "|" '  - ' "|",
#     "-----------------------------------------------------------------------------------"
#     "|"' - ',"|" ' - ', "|" ' - ', "|" '-', "|" '-', "|" ' - ', "|" ' -',  "|" '  - ' "|",
#     "-----------------------------------------------------------------------------------"
#     "|"' - ',"|" ' - ', "|" ' - ', "|" '-', "|" '-', "|" ' - ', "|" ' -',  "|" '  - ' "|",
#     "-----------------------------------------------------------------------------------"
#     "|"' - ',"|" ' - ', "|" ' - ', "|" '-', "|" '-', "|" ' - ', "|" ' -',  "|" '  - ' "|",
#     "-----------------------------------------------------------------------------------"
#     "|"' S ',"|" ' S ', "|" ' S ', "|" 'S', "|" 'S', "|" ' S ', "|" ' S',  "|" '  S ' "|",
#     "-----------------------------------------------------------------------------------"
#     "|"'E_L',"|" 'H_L', "|" 'M_L', "|" 'Q', "|" 'K', "|" 'M_R', "|" 'H_R', "|"  'E_R' "|"
#     "-----------------------------------------------------------------------------------"
# ]
# # print("\nChess Board:\n")
# # for row in new_board:
# if(row == 5):
#     print("\n")
# print(new_board)
