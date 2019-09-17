import random
import string

def printe(arr):
    for i in range(0,3):
        for j in range(0,3):
            print("|"+str(bord[i][j])+"| ",end=" ")
        print('\n')

def checkWin(arr,i,j,ch):
    val=0
    for k in range(0,3):
        if(arr[i][k]==ch):
            val+=1
        else:
            val=0
            break
    if (val == 3):
        return True

    for l in range(0,3):
        if(arr[l][j]==ch):
            val+=1
        else:
            val=0
            break
    if (val == 3):
        return True
    q=2
    for t in range(0,3):
        if(arr[t][q]==ch):
            val+=1
            q-=1
        else:
            val=0
            break
    if(val==3):
        return True
    w=0
    for e in range(0,3):
        if(arr[e][w]==ch):
            val+=1
            w+=1
        else:
            val=0
            break
    if (val == 3):
        return True

    return False

def sett(arr,i,j,ch):
    arr[i][j]=ch

def check2(arr,i,j,ch1,ch2):
    if arr[i][j]==ch1 or arr[i][j]==ch2:
        return False
    else:
        return True

def checkforSub (arr,i,j):
    if arr[i][j]==(' '):
        return True
    else:
        return False
def havanakan(arr,i,j,):
    global porc
    val=0
    for k in range(0,3):
        if arr[k][j]==' ':
            val+=1
        else:
            val=0
            break
    if(val==3):
        porc+=1
        return True
    for l in range(0,3):
        if arr[i][l]==' ':
            val+=1
        else:
            val=0
            break
    if (val == 3):
        porc+=1
        return True
    q=0
    for  y in range(0,3):
        if arr[y][q]==' ':
            val+=1
            q+=1
        else:
            val=0
            break
    if (val == 3):
        porc+=1
        return True
    w=2
    for y2 in range(0,3):
        if arr[y2][w]==' ':
            val+=1
            w-=1
        else:
            val=0
            break;
    if (val == 3):
        porc+=1
        return True

    return False

def ifcanWin(arr,k,l,ch):
    havan=0;
    listt=[]

    for j in range(0,3):
        if arr[k][j]==ch:
            havan+=1
    if(havan==2):
        listt.append(2-k)

def full(arr):
    val=0
    for i in range(0,3):
        for j in range(0,3):
            if arr[i][j]!=(' '):
                val+=1
    if val==9:
        return False
    else:
        return True

def intelect1(arr,i,j,ch):
      if arr[1][1]==(' '):
          return 1
      else:
          if arr[1][1]==ch:
              return 2

def closetoWin(arr, ch):
    li=[]
    j = 0
    val = 0
    pt = 0
    for i in range(0, 3):
        for k in range(0, 3):
            if arr[i][k] == ch:
                val += 1

        if val == 2:
            for l in range(0, 3):
                if arr[i][l] == (' '):
                    pt = l
                    li.append(i)
                    li.append(l)
                    return li
        else:
            val=0

    for i in range(0, 3):
        for k in range(0, 3):
            if arr[k][i] == ch:
                val += 1
        if val == 2:
            for l in range(0, 3):
                if arr[l][i] == (' '):
                    li.append(l)
                    li.append(i)
                    return li
        else:
            val=0

    k = 0
    for i in range(0, 3):
        if arr[i][k] == ch:
            val += 1
        k+=1

    if val == 2:
        g = 0
        for i in range(0, 3):
            if arr[i][g] == (' '):
                li.append(i)
                li.append(g)
                return li
            else:
                g += 1
    else:
        val=0
    k = 0
    l=2
    for i in range(0,3):
        if arr[k][l] == ch:
            val += 1
        k += 1
        l-=1
    if val == 2:
        k = 0
        l=2
        for i in range(0, 3):
            if arr[k][l] == (' '):
                li.append(k)
                li.append(l)
                return li
            else:
                k += 1
                l-=1
    else:
        val=0
    if val==0:
        li.append(10)
        li.append(10)
        return li

def TriangelWin(arr,ch):
    li=[]
    if arr[0][0]==ch:
        if arr[1][1]==ch:
            if(stugel2(arr,2,0,'X','0')):
                li.append(2)
                li.append(0)
            else:
                li.append(0)
                li.append(2)
            return li
    elif arr[2][0]==ch:
        if arr[1][1]==ch:
            if stugel2(arr,0,0,'X','0'):
                li.append(0)
                li.append(0)
            else:
                li.append(2)
                li.append(0)
            return li
    elif arr[0][2]==ch:
        if arr[1][1]==ch:
            if stugel2(arr,0,0,'X','0'):
                li.append(0)
                li.append(0)
            else:
                li.append(2)
                li.append(0)
            return li
    elif arr[2][2]==ch:
        if arr[1][1]==ch:
            if stugel2(arr,0,2,'X','0'):
                li.append(0)
                li.append(2)
            else:
                li.append(2)
                li.append(0)
            return li
    else:
        li.append(10)
        li.append(10)

lis=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
bord=[[],[],[]]
chi=0
qanak=0
for i in range(0, 3):
    for j in range(0, 3):
        bord[i].append(' ')

start=int(input("To play 2 players pres-1, to play with BOT pres-2"))
if start==1:
    qa=0
    while full(bord):
        qa+=1
        b = 'X'
        t = '0'
        while True:
            inp=input("Type coordinates for Player 1")
            inp=inp.translate({ord(c): None for c in string.whitespace})
            y = int(inp[0])
            g = int(inp[1])
            if(check2(bord,y,g,b,t)):
                sett(bord,y,g,b)
                printe(bord)
                if(checkWin(bord,y,g,b)):
                    print("Player 1 Win")
                    chi=1
                    break
                break
            else:
                print("wrong coordinats please type again")
        if chi==1:
            break
        while True:
            inp=input("type coordinates for Player 2")
            inp=inp.translate({ord(c): None for c in string.whitespace})
            y1 = int(inp[0])
            g1 = int(inp[1])
            if (check2(bord, y1, g1, b, t)):
                sett(bord, y1, g1, t)
                printe(bord)
                if (checkWin(bord, y1, g1, b)):
                    print("Player 2 Win")
                    break
                break
            else:
               print("wrong coordinats please type again")
        if chi==1:
            break

else:
    qw=0
    que=0
    lis2 = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    print("START!!!!")
    b = 'X'
    t = '0'
    while full(bord):
        while True:
            inp=input("PRES COORDINATES PLEASE")
            inp=inp.translate({ord(c): None for c in string.whitespace})
            x1=int(inp[0])
            y1=int(inp[1])
            ind1 = 0
            if(check2(bord,x1,y1,b,t)):
                for i in range(0, len(lis2)):
                    if x1 == lis2[i][0] and y1 == lis2[i][1]:
                        ind1 = i
                        break
                lis2.pop(ind1)
                sett(bord,x1,y1,b)
                if(checkWin(bord,x1,y1,b)):
                    print("OH NO YOU WIN!!!")
                    qw=1
                    break
                break
            else:
                print("WRONG COORDINATES TYPE AGAIN!")
        if qw==1:
            print("THE END!")
            break
        kr1=x1
        kr2=y1
        x2=0
        y2=0
        if que==0:
            if intelect1(bord,kr1,kr2,b)==2:
                r=random.randrange(0,2)
                if r==0:
                    x2=0
                    y2=0
                else:
                    x2=2
                    y2=2
                sett(bord,x2,y2,t)
                ind = 0
                for i in range(0, len(lis2)):
                    if x2 == lis2[i][0] and y2 == lis2[i][1]:
                        ind = i
                        break
                lis2.pop(ind)
                printe(bord)
                que+=1
            elif intelect1(bord,kr1,kr2,b)==1:
                x2=1
                y2=1
                sett(bord,x2,y2,t)
                que+=1
                ind = 0
                for i in range(0, len(lis2)):
                    if x2 == lis2[i][0] and y2 == lis2[i][1]:
                        ind = i
                        break
                lis2.pop(ind)
                printe(bord)
        elif que==1:
            pl=closetoWin(bord,b)
            if pl[0]!=10:
                x2=pl[0]
                y2=pl[1]
                sett(bord,x2,y2,t)
                que+=1
                ind=0
                for i in range(0, len(lis2)):
                    if x2 == lis2[i][0] and y2 == lis2[i][1]:
                        ind = i
                        break
                lis2.pop(ind)
                printe(bord)
            elif True:
                pl2 = TriangelWin(bord, b)
                if pl2!=None:
                    if pl2[0] != 10:
                        x2 = pl2[0]
                        y2 = pl2[1]
                        sett(bord, x2, y2, t)
                        ind = 0
                        for i in range(0, len(lis2)):
                            if x2 == lis2[i][0] and y2 == lis2[i][1]:
                                ind = i
                                break
                        lis2.pop(ind)
                        printe(bord)
                else:
                    xr = random.randrange(0, len(lis2))
                    x2 = lis2[xr][0]
                    y2 = lis2[xr][1]
                    lis2.pop(xr)
                    sett(bord, x2, y2, t)
                    que += 1
                    printe(bord)
            else:
                xr=random.randrange(0,len(lis2))
                x2=lis2[xr][0]
                y2=lis2[xr][1]
                lis2.pop(xr)
                sett(bord,x2,y2,t)
                que+=1
                printe(bord)
        elif que==2:
            pl=closetoWin(bord,t)
            if pl!=None:
                if pl[0]!=10:
                    x2=pl[0]
                    y2=pl[1]
                    sett(bord,x2,y2,t)
                    ind = 0
                    for i in range(0, len(lis2)):
                        if x2 == lis2[i][0] and y2 == lis2[i][1]:
                            ind = i
                            break
                    lis2.pop(ind)
                    printe(bord)
                    if checkWin(bord,x2,y2,t):
                        print("I WIN GOODBYE :)")
                        break
                else:
                    pl=TriangelWin(bord,b)
                    if pl[0]!=10:
                        x2=pl[0]
                        y2=pl[1]
                        sett(bord, x2, y2, t)
                        ind = 0
                        for i in range(0, len(lis2)):
                            if x2 == lis2[i][0] and y2 == lis2[i][1]:
                                ind = i
                                break
                        lis2.pop(ind)
                        printe(bord)
                        if checkWin(bord, x2, y2, t):
                            print("I WIN GOODBYE :)")
                            break
                    else:
                        xr = random.randrange(0, len(lis2))
                        x2 = lis2[xr][0]
                        y2 = lis2[xr][1]
                        lis2.pop(xr)
                        sett(bord, x2, y2, t)
                        que += 1
                        printe(bord)
                        if checkWin(bord, x2, y2, t):
                            print("I WIN GOODBYE :)")
                            break
            elif pl==None:
                print("This is the one way to win me :)")
                print("You win")
                break
        else:
            pl=closetoWin(bord,t)
            if pl[0]!=10:
                x2 = pl[0]
                y2 = pl[1]
                sett(bord, x2, y2, t)
                ind = 0
                for i in range(0, len(lis2)):
                    if x2 == lis2[i][0] and y2 == lis2[i][1]:
                        ind = i
                        break
                lis2.pop(ind)
                printe(bord)
                if checkWin(bord, x2, y2, t):
                    print("I WIN GOODBYE :)")
                    break
            else:
                    pl=closetoWin(bord,b)
                    if pl[0]!=10:
                        x2=pl[0]
                        y2=pl[1]
                        sett(bord, x2, y2, t)
                        ind = 0
                        for i in range(0, len(lis2)):
                            if x2 == lis2[i][0] and y2 == lis2[i][1]:
                                ind = i
                                break
                        lis2.pop(ind)
                        printe(bord)
                        if checkWin(bord, x2, y2, t):
                            print("I WIN GOODBYE :)")
                            break
                            taxtak=0

