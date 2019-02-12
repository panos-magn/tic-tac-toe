def check(t,typ):
    return ((t[1]==typ and t[2]==typ and t[3]==typ)or(t[1]==typ and t[4]==typ and t[7]==typ)or(t[1]==typ and t[5]==typ and t[9]==typ)or(t[2]==typ and t[5]==typ and t[8]==typ)or(t[7]==typ and t[8]==typ and t[9]==typ)or(t[3]==typ and t[6]==typ and t[9]==typ)or(t[3]==typ and t[5]==typ and t[7]==typ)or(t[4]==typ and t[5]==typ and t[6]==typ))
def loop(t,player,symbol,t1):
    t1=False
    if t[player]==" ":
        t[player]=symbol
        t1=True
    return t1       

def myfuc(t):
    print "----","----","---"   
    print "|",t[1],"|", t[2],"|",t[3],"|"
    print "----","----","---"
    print "|",t[4],"|",t[5],"|",t[6],"|"
    print "----","----","---"
    print "|",t[7],"|",t[8],"|",t[9],"|"
    print "----","----","---"
turn=0        
t=10*[" "]    
myfuc(t)
s="O"
s1="X"
print ("do you want to play tic tac toe??write 1 or 0")
game=input()
while( (check(t,s)!=True)and(check(t,s1)!=True))and(turn<=10)and(game==1):
    if turn%2==0 or turn==0:
        
        print ("give me a position of this table,where you want to play")
        player=input()
        t1=False
        if t[player]!=" ":
            while t1==False  :
                player=input()
                t1=loop(t,player,s,t1)
                
        else: 
            loop(t,player,s,t1)
        myfuc(t)
        turn=turn+1
    else:
       symbol="X"
       i=1
       while i<=9:
           if t[i]==" " :
                t[i]=symbol
                myfuc(t)
                i=i+9
           i=i+1
       turn=turn+1
    if (turn==9)or(check(t,s)==True) or(check(t,s1)==True):
        if (check(t,s)==True):
            print("you win")
        elif (check(t,s1)==True):
            print ("you lose")
        else:
            print("nobody win this game")
        print("do you want to play again ?? write 1 or 0")
        game=input()
