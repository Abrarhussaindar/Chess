board = [
    ['B_L_E', 'B_L_H', 'B_L_C', 'B_Q', 'B_K', 'B_R_C', 'B_R_H', 'B_R_E'],
    [' S ', ' S ', ' S ', 'S', 'S', ' S ', ' S ', ' S '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' - ', ' - ', ' - ', '-', '-', ' - ', ' - ', ' - '],
    [' S ', ' S ', ' S ', 'S', 'S', ' S ', ' S ', ' S '],
    ['E_L', 'H_L', 'M_L', 'Q', 'K', 'M_R', 'H_R', 'E_R']
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

enemy_pieces = ["B_L_E", "B_L_H", "B_L_C", "B_Q", "B_K", "B_R_C", "B_R_H", "B_R_E"]

# pieces = {
    # 'B_L_E': 
# }
def check_enemy_pieces():
    for i in range(0, len(enemy_pieces)):
        return enemy_pieces[i]

def check_adjecent_piece():
    for adj_piece in board:
        while("W_K" != adj_piece):
            if check_enemy_pieces() == adj_piece:
                return True

def CheckMate():
    i=7
    j=4
    for row in range(0,8):
        for col in range(0,8):
            if check_enemy_pieces() == board[row][col]:
                # check_adjecent_piece() ==  
                pass

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
CheckMate()
    # print_indicies()
    # # input_piece()
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
