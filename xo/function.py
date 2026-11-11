from xo.input import *

def try_number(n):
    while True:
        num = input("tap were you want to put")   
        if num not in ["1","2","3","4","5","6","7","8","9"]:
            print("error!" \
            "You must enter a positive number from 1 to 9. try again.") 
        elif n[int(num)-1] == " x " or n[int(num)-1] == " o ":
            print("This slot is taken.")
        else:
            return num

    

def chek(base, win):
    winer(win)
    if winer(win) == "win":
        return "win"

    for i in base:
        if i == " o " or i == " x ":
            continue
        return
    return "end"

def winer(list_num):
    WINNING_LINES = [
(0, 1, 2),
(3, 4, 5),
(6, 7, 8),
(0, 3, 6),
(1, 4, 7),
(2, 5, 8),
(0, 4, 8),
(2, 4, 6),]
    for i in WINNING_LINES:
        if i[0] in list_num and i[1] in list_num and i[2] in list_num:
            return "win"
            
            
    

    
            
        


