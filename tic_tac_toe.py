for _ in range(int(input())):
    l=[]
    x,o=0,0
    l.append(input())
    l.append(input())
    l.append(input())
    for i in l:
        for j in i:
            if j == 'X':
                x+=1
            elif j == 'O':
                o+=1
    xx = True if((l[0]== "XXX") or (l[1]== "XXX") or(l[2]== "XXX") or(l[0][0]==l[1][0]==l[2][0]=='X') or (l[0][1]==l[1][1]==l[2][1]=='X') or (l[0][2]==l[1][2]==l[2][2]=='X') or (l[0][0]==l[1][1]==l[2][2]=='X') or (l[0][2]==l[1][1]==l[2][0]=='X')) else False
    oo = True if((l[0]== "OOO") or (l[1]== "OOO") or(l[2]== "OOO") or(l[0][0]==l[1][0]==l[2][0]=='O') or (l[0][1]==l[1][1]==l[2][1]=='O') or (l[0][2]==l[1][2]==l[2][2]=='O') or (l[0][0]==l[1][1]==l[2][2]=='O') or (l[0][2]==l[1][1]==l[2][0]=='O')) else False
    if((xx and oo) or abs(x-o)>1) or (xx and(o>=x)) or (oo and (o!=x)) or (x<o):
        print("3")
    elif xx or oo or x+o ==9:
        print("1")
    else:
        print("2")