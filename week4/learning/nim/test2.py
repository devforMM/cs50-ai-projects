dictionnaire={
    ((0, 0, 0, 2), (3, 2)): 1 ,
    ((0, 0, 0, 2), (3, 2)): 22,
    ((0, 0, 0, 2), (3, 2)): 100,
    ((0, 0, 0, 2), (3, 2)): 99
    

}


state=[0, 0, 0, 2]
action=(3,2)



t=(0,0,0,2)

print(state==list(t))

def get_q(s,a):
    for k in dictionnaire.keys():
        if s==list(k[0]) and a==k[1]:
            print(dictionnaire[(tuple(s),a)])
    

get_q(state,action)