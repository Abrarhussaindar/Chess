board = [
    ['B_L_E', 'B_L_H', 'B_L_C', 'B_Q', 'B_K', 'B_R_C', 'B_R_H', 'B_R_E'],
    [' B_S ', ' B_S ', ' B_S ', 'B_S', 'B_S', ' B_S ', ' B_S ', ' B_S '],
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
class Pieces:
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

for obj in Black_piece_list:
    print(obj.name)
    if obj.name == "B_L_E":
        print(obj.ist_index, obj.second_index)

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

for obj in White_piece_list:
    print(obj.name)

# print(e1.name)
# print()
# enemy_pieces = ["B_L_E", "B_L_H", "B_L_C", "B_Q", "B_K", "B_R_C", "B_R_H", "B_R_E"]
list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(3):
    for j in range(3):
        # print(list[i][j
        # while(j<1 and i<1):
            # print(list[i][j])
        print(list[i][j])
        if i==1 and j==1:
            break
# print(list[0])
# pieces = {
    # 'B_L_E': 
# }
def check_enemy_pieces():
    for i in range(0, len(Black_piece_list)):
        return Black_piece_list[i]

def check_adjecent_piece():
    for adj_piece in board:
        while("W_K" != adj_piece):
            if check_enemy_pieces() == adj_piece:
                return True

# def CheckMate():
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

    if(index_to_2 < 3 or index_to_2 > 4):
        board[index_from_1][index_from_2] = ' - '
    else:
        board[index_from_1][index_from_2] = '-'

    # return index_1, index_2
# while(True):
# CheckMate()
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
