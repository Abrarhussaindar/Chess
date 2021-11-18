board = [
    ['B_L_E', 'B_L_H', 'B_L_C', 'B_Q', 'B_K', 'B_R_C', 'B_R_H', 'B_R_E'],
    ['B_S', 'B_S', 'B_S', 'B_S', 'B_S', 'B_S', 'B_S', 'B_S'],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' - ', ' - ', ' - ', '', '-', ' - ', ' - ', ' - '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' S ', ' S ', ' S ', 'S', 'S', ' S ', ' S ', ' S '],
    ['E_L', 'H_L', 'M_L', 'Q', 'W_K', 'M_R', 'H_R', 'E_R']
]

def print_board():
    print("\nChess Board:\n")
    for row in board:
        print(row)
print_board()

# class Pieces:
#     def __init__(self):
#         self.ist_index = 0
#         self.second_index = 0
        
# p = Pieces()
# print(p.ist_index)

# Pieces = {
#     "B_E": 
# }

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

enemy_pieces = ["B_L_E", "B_L_H", "B_L_C", "B_Q", "B_K", "B_R_C", "B_R_H", "B_R_E", "B_S"]

# pieces = {
    # 'B_L_E': 
# }
def check_enemy_pieces(row, col):
    for i in range(0, len(enemy_pieces)):
        # print(enemy_pieces[i])
        if enemy_pieces[i] == board[row][col]:
            # print("4 true")
            # print(enemy_pieces[i])
            return enemy_pieces[i]

def check_adjecent_piece(row, col):
    for piece in board:
        # print("col", col)
        # while("W_K" != piece[row]):
        if check_enemy_pieces(row, col) == piece[row+1]:
            print("row ", str(row) + " " + str(col))
            # print("adj", piece[row+1])
            return piece[row+1]
        # elif check_enemy_pieces(row, col) ==  piece[col+1]:
        #     return piece[col+1]

def CheckMate():
    # i=7
    # j=4
    for row in range(8):
        # print(row)
        for col in range(8):
            # print("ele",board[row][col])
            if check_enemy_pieces(row, col) == board[row][col]:
                if "B_L_E" == board[row][col]:
                    # print("treue")
                    for i in range(8):
                        for j in range(8):
                            if i == j == 1:
                                break
                            elif i == 2 and j == 1:
                                break
                            elif i == 3 and j == 1:
                                break
                            elif i == 4 and j == 1:
                                break
                            elif i == 5 and j == 1:
                                break
                            elif i == 6 and j == 1:
                                break
                            elif i == 7 and j == 1:
                            # while(i<1 and j<1):
                                break
                            # print(i,
                            if check_adjecent_piece(i,j):
                                print("true")
                                # break
                # print(piece)
                # print("1 true at row "+ str(row) + " col " + str(col) + " piece " + board[row][col])
                # print("at col " + str(col) + " piece " + check_enemy_pieces(row, col))
                # piece = check_adjecent_piece(row, col)
                # print(piece)
                    
                    # pass
                    # print("true", check_adjecent_piece(row, col))
                    # print("2 true")
                    # pass
            # break

                    
            # else:
            #     print(check_enemy_pieces(row, col))
            #     print("not enemy piece")

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

    if(index_to_2 < 3 or index_to_2 > 4):
        board[index_from_1][index_from_2] = ' - '
    else:
        board[index_from_1][index_from_2] = '-'

    # return index_1, index_2
# while(True):

print_indicies()
CheckMate()
# input_piece()
    # input_indicies()
    # print_board()
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
