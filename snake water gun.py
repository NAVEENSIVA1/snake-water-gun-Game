import random
num=int(input("ENTER THE NUMBER OF ROUNDS:"))
player1=0
player2=0
option=['s','w','g']
print("snake-s")
print("water-w")
print("gun-g")
for i in range(num):
    print("ROUND:",i+1)
    m=input("ENTER YOUR OPTION:")
    n=random.choice(option)
    if m==n:
        print("Draw")
        player1=0
        player2=0
    elif m=="s" and n=="w":
        print("YOU GOT ONE POINT")
        player1+=1
    elif m=="s" and n=="g":
        print("OPPONENT GOT ONE POINT")
        player2+=1
    elif m=="g" and n=="w":
        print("OPPONENT GOT ONE POINT")
        player2+=1
    elif m=="w" and n=="s":
        print("OPPONENT GOT ONE POINT")
        player2+=1
    elif m=="g" and n=="s":
        print("YOU GOT ONE POINT")
        player1+=1
    elif m=="w" and n=="g":
        print("YOU GOT ONE POINT")
        player1+=1
print("end")
if player1>player2:
    print("YOU WON")
elif player1<player2:
    print("YOU LOOSE")
else:
    print("THE GAME IS DRAW")

print("G@ME 0VER!")
