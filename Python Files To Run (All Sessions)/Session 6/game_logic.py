
# #   0  |  1  |  2   
# # =================
# #   3  |  4  |  5
# # =================
# #   6  |  7  |  8



# B = [" ", " ", " "," ", " ", " "," ", " ", " "]

   
result = ""
def win_check(B):
    global result
    if B[0]=='X' and B[1] =='X' and B[2] =='X':
        result = "x won"
        return result
    elif B[0] == 'X' and B[4] == 'X' and B[8] == 'X':
        result = "x won"
        return result
    elif B[0] == 'X' and B[3] == 'X' and B[6] == 'X':
        result = "x won"
        return result
    elif B[2] == 'X' and B[4] == 'X' and B[6] == 'X':
        result = "x won"
        return result
    elif B[1] == 'X' and B[4] == 'X' and B[7] == 'X':
        result = "x won"
        return result
    elif B[2] == 'X' and B[5] == 'X' and B[8] == 'X':
        result = "x won"
        return result
    elif B[6] == 'X' and B[7] == 'X' and B[8] == 'X':
        result = "x won"
        return result
    elif B[3] == 'X' and B[4] == 'X' and B[5] == 'X':
        result = "x won"
        return result

    elif B[0] == 'O' and B[1] == 'O' and B[2] == 'O':
        result = "o won"
        return result
    elif B[0] == 'O' and B[4] == 'O' and B[8] == 'O':
        result = "o won"
        return result
    elif B[0] == 'O' and B[3] == 'O' and B[6] == 'O':
        result = "o won"
        return result
    elif B[2] == 'O' and B[4] == 'O' and B[6] == 'O':
        result = "o won"
        return result
    elif B[1] == 'O' and B[4] == 'O' and B[7] == 'O':
        result = "o won"
        return result
    elif B[2] == 'O' and B[5] == 'O' and B[8] == 'O':
        result = "o won"
        return result
    elif B[6] == 'O' and B[7] == 'O' and B[8] == 'O':
        result = "o won"
        return result
    elif B[3] == 'O' and B[4] == 'O' and B[5] == 'O':
        result = "o won"
        return result
    print(B)
    
