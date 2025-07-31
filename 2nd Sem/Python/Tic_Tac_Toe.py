cheat = [0,0,0,0,0,0,0,0,0]
X_O = [" "," "," "," "," "," "," "," "," "]
a=1

def check():
    a1,a2,a3,b1,b2,b3,c1,c2,c3 = X_O
    if (a1==a2==a3=='X') or (b1==b2==b3=='X') or (c1==c2==c3=='X') or (a1==b1==c1=='X') or (a2==b2==c2=='X') or (a3==b3==c3=='X') or (a1==b2==c3=='X') or (a3==b2==c1=='X'):
            X_win()
    elif(a1==a2==a3=='O') or (b1==b2==b3=='O') or (c1==c2==c3=='O') or (a1==b1==c1=='O') or (a2==b2==c2=='O') or (a3==b3==c3=='O') or (a1==b2==c3=='O') or (a3==b2==c1=='O'):
            O_win()
    
def X_win():
    out()
    print("-----Player 1 Wins-----")
    game_over()
    
def check_cheat(x):
    if cheat[x-1] == 0:
        cheat[x-1] = 1
    else:
        print("Don't  Cheat")
        Start()
    
def O_win():
    out()
    print("-----Player 2 Wins-----")
    game_over()
    
def inva():
    print("PLZ ENTER A VALUE")
    Start()
    
def mark_X(x):
    X_O[x-1]='X'
    Start()

def mark_O(x):
    X_O[x-1] = 'O'
    Start()

def check_valid(ck):
    if(ck > 9 or ck <= 0):
        print("Invalid Place")
        Start()

def Start():
    global a
    
    if(a==10):
        game_over()
        
    elif (a%2!=0):
        check()
        print("Player 1 turn")
        out()
        ip = int(input("Enter The Place To Mark: ") or inva())
        check_valid(ip)
        check_cheat(ip)
        a+=1
        mark_X(ip)
        
    elif (a%2== 0):
        check()
        print("Player 2 turn")
        out()
        ip = int(input("Enter The Place To Mark: ") or inva())
        check_valid(ip)
        check_cheat(ip)
        a+=1
        mark_O(ip)

def  game_over():
    print("Game Over")
    menu()

def ent():
    print("PLZ")
    menu()

def out():
    print("  {}  |  {}  |  {}  \n────────────────\n  {}  |  {}  |  {}  \n────────────────\n  {}  |  {}  |  {}  ".format(X_O[0],X_O[1],X_O[2],X_O[3],X_O[4],X_O[5],X_O[6],X_O[7],X_O[8]))
def menu():
    i = 0
    global X_O,a,cheat
    cheat = [0,0,0,0,0,0,0,0,0]
    X_O = [" "," "," "," "," "," "," "," "," "]
    a=1
    print("Welcome!\n1:Start Game\n2:Exit")
    i = int(input("Enter Your Choice(1|2): ") or ent())
    if i == 1:
        Start()
    elif i == 2:
        exit()
    else:
        print("Invalid input")
        menu()
menu()