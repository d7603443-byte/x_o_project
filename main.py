from xo.input import *
from xo.function import *

base = basic()
up = update(base)
num_x = []
num_o = []
print(up)

while True:
    p_x = player_x()
    a = try_number(base)
    base[int(a)-1] = " x "
    num_x.append(int(a)-1)
    up = update(base)
    print(up)
    x = chek(base, num_x)
    if x == "end":
        print ("\n The game is over, a draw.")
        break
    elif x == "win":
        print ("\n Congratulations, you've won the game.")
        break
    


   
    p_o = player_o()
    a = try_number(base)
    base[int(a)-1] = " o "
    num_o.append(int(a)-1)
    up = update(base)
    print(up)
    o = chek(base, num_o)
    if o == "end":
        print ("\n The game is over, a draw.")
        break
    elif o == "win":
        print ("\n Congratulations, you've won the game.")
        break




    