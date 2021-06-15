l1="abcdefghijklm"
l2="NOPQRSTUVWXYZ"
for _ in range(int(input())):
    fl="YES"
    s=input().split()
    for i in s[1:]:
        if(i[0] in l1):
            for l in i:
                if(l not in l1):
                    fl="NO"
                    break
        elif(i[0] in l2):
            for l in i:
                if(l not in l2):
                    fl="NO"
                    break
        else:
            fl="NO"
            break
        if(fl=="NO"):
            break
    print(fl)
        
    
