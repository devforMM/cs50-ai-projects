grille = [["_" for _ in range(3)] for _ in range(3)]

grille[1][1]="X"
grille[2][2]="d"


x_pos,y_pos=0,0
def mouvements_disponibles(i, j):
    mouvements = []
    if i > 0:
        mouvements.append("haut")
    if i < 2:
        mouvements.append("bas")
    if j > 0:
        mouvements.append("gauche")
    if j < 2:
        mouvements.append("droite")
    return mouvements

def dep(m,i,j):
    if m=="droite" and m in mouvements_disponibles(i,j):
        j+=1
        return i,j
    elif m=="gauche" and m in mouvements_disponibles(i,j):
        j-=1
        return  i,j
    elif m=="bas" and m in mouvements_disponibles(i,j):
        i+=1
        return i,j 
    elif m=="haut" and m in mouvements_disponibles(i,j):
        i-=1
        return i,j
    
states=[]
for i in range(3):
    for j in range(3):
        states.append((i,j)) 
memoire={
}
for s in states:
    memoire[s]=[]
    for m in mouvements_disponibles(s[0],s[1]):
        memoire[s].append((m,0))

def reward(i,j,direction):
    if grille[i][j]=="X":
        return -10
    elif grille[i][j]=="d":
        return 10
    elif (i,j) in explored:
        return -5
    else:
        return 1

def update():
    for i in range(len(memoire[s])):
        if memoire[s][i][0]==direction:
            new_value=memoire[s][i][1]+alpha*(r+q_val-memoire[s][i][1])
            memoire[s][i]=(memoire[s][i][0],new_value)

alpha=0.5

game_over=None
loses=0
while True:
    s=(0,0)
    explored=[]
    while True:
            print(f"notre position est {s}")
            explored.append(s)
            direction=max(memoire[s],key=lambda x: x[1])[0]
            print(f"je me deplace vers {direction}")
            new_state=dep(direction,s[0],s[1])
            print(f"je suis arrive a {new_state}")
            r=reward(new_state[0],new_state[1],direction)
            q_val=max(memoire[new_state])[1]
            update()
            s=new_state
            if s==(2,2):
                print("gagner")
                game_over=True
                break
            if s==(1,1):
                print("bomm perdu")
                loses
                break
    if game_over==True:
        break
    
    
print(f"tu as perdu {loses} fois avant de gagner")















        














