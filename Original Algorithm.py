import numpy as np
import sys


dict={}
dict["normal"]=np.array([0,-1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
dict["fighting"]=np.array([0,0,-1,0,0,1,1,0,0,0,0,0,0,-1,0,0,1,-1,0])
dict["flying"]=np.array([0,1,0,0,2,-1,1,0,0,0,0,1,-1,0,-1,0,0,0,0])
dict["poison"]=np.array([0,1,0,1,-1,0,1,0,0,0,0,1,0,-1,0,0,0,1,0])
dict["ground"]=np.array([0,0,0,1,0,1,0,0,0,0,-1,-1,1,0,-1,0,0,0,0])
dict["rock"]=np.array([1,-1,1,1,-1,0,0,0,-1,1,-1,-1,0,0,0,0,0,0,0])
dict["bug"]=np.array([0,1,-1,0,1,-1,0,0,0,-1,0,1,0,0,0,0,0,0,0])
dict["ghost"]=np.array([2,1,0,1,0,0,1,-1,0,0,0,0,0,0,0,0,-1,0,0])
dict["steel"]=np.array([1,-1,1,2,-1,1,1,0,1,-1,0,1,0,1,1,1,0,1,0])
dict["fire"]=np.array([0,0,0,0,-1,-1,1,0,1,1,-1,1,0,0,1,0,0,1,0])
dict["water"]=np.array([0,0,0,0,0,0,0,0,1,1,1,-1,-1,0,1,0,0,0,0])
dict["grass"]=np.array([0,0,-1,-1,1,0,-1,0,0,-1,1,1,1,0,-1,0,0,0,0])
dict["electric"]=np.array([0,0,1,0,-1,0,0,0,1,0,0,0,1,0,0,0,0,0,0])
dict["psychic"]=np.array([0,1,0,0,0,0,-1,-1,0,0,0,0,0,1,0,0,-1,0,0])
dict["ice"]=np.array([0,-1,0,0,0,-1,0,0,-1,-1,0,0,0,0,1,0,0,0,0])
dict["dragon"]=np.array([0,0,0,0,0,0,0,0,0,1,1,1,1,0,-1,-1,0,-1,0])
dict["dark"]=np.array([0,-1,0,0,0,0,-1,1,0,0,0,0,0,2,0,0,1,-1,0])
dict["fairy"]=np.array([0,1,0,-1,0,0,1,0,-1,0,0,0,0,0,0,2,1,0,0])
dict["none"]=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

value={}
value[0]="Normal"
value[1]="Fighting"
value[2]="Flying"
value[3]="Poison"
value[4]="Ground"
value[5]="Rock"
value[6]="Bug"
value[7]="Ghost"
value[8]="Steel"
value[9]="Fire"
value[10]="Water"
value[11]="Grass"
value[12]="Electric"
value[13]="Psychic"
value[14]="Ice"
value[15]="Dragon"
value[16]="Dark"
value[17]="Fairy"

test={}
test["normal"]=0
test["fighting"]=1
test["flying"]=2
test["poison"]=3
test["ground"]=4
test["rock"]=5
test["bug"]=6
test["ghost"]=7
test["steel"]=8
test["fire"]=9
test["water"]=10
test["grass"]=11
test["electric"]=12
test["psychic"]=13
test["ice"]=14
test["dragon"]=15
test["dark"]=16
test["fairy"]=17

#strengths
nor=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
fig=np.array([1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0])
fly=np.array([0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0])
poi=np.array([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0])
gro=np.array([0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0])
roc=np.array([0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0])
buu=np.array([0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0])
gho=np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0])
ste=np.array([0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0])
fir=np.array([0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0])
wat=np.array([0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0])
gra=np.array([0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0])
ele=np.array([0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
psy=np.array([0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
icc=np.array([0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0])
dra=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
dar=np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0])
fai=np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0])

#weaknesses/resistances + strengths
normal=np.array([0,-1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]) + nor
fighting=np.array([0,0,-1,0,0,1,1,0,0,0,0,0,0,-1,0,0,1,-1,0]) + fig
flying=np.array([0,1,0,0,1,-1,1,0,0,0,0,1,-1,0,-1,0,0,0,0]) + fly
poison=np.array([0,1,0,1,-1,0,1,0,0,0,0,1,0,-1,0,0,0,1,0]) + poi
ground=np.array([0,0,0,1,0,1,0,0,0,0,-1,-1,1,0,-1,0,0,0,0]) + gro
rock=np.array([1,-1,1,1,-1,0,0,0,-1,1,-1,-1,0,0,0,0,0,0,0]) + roc
bug=np.array([0,1,-1,0,1,-1,0,0,0,-1,0,1,0,0,0,0,0,0,0]) + buu
ghost=np.array([1,1,0,1,0,0,1,-1,0,0,0,0,0,0,0,0,-1,0,0]) + gho
steel=np.array([1,-1,1,1,-1,1,1,0,1,-1,0,1,0,1,1,1,0,1,0]) + ste
fire=np.array([0,0,0,0,-1,-1,1,0,1,1,-1,1,0,0,1,0,0,1,0]) + fir
water=np.array([0,0,0,0,0,0,0,0,1,1,1,-1,-1,0,1,0,0,0,0]) + wat
grass=np.array([0,0,-1,-1,1,0,-1,0,0,-1,1,1,1,0,-1,0,0,0,0]) + gra
electric=np.array([0,0,1,0,-1,0,0,0,1,0,0,0,1,0,0,0,0,0,0]) + ele
psychic=np.array([0,1,0,0,0,0,-1,-1,0,0,0,0,0,1,0,0,-1,0,0]) + psy
ice=np.array([0,-1,0,0,0,-1,0,0,-1,-1,0,0,0,0,1,0,0,0,0]) + icc
dragon=np.array([0,0,0,0,0,0,0,0,0,1,1,1,1,0,-1,-1,0,-1,0]) + dra
dark=np.array([0,-1,0,0,0,0,-1,1,0,0,0,0,0,1,0,0,1,-1,0]) + dar
fairy=np.array([0,1,0,-1,0,0,1,0,-1,0,0,0,0,0,0,1,1,0,0]) + fai
none=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])



print("What Pokemon are you using? (put none for type 2 if monotype)\n")
print("First Pokemon:")
type11=input("First type? (no caps): ")
type(type11)
type12=input("Second type? (no caps): ")
type(type12)
print("")
print("Second Pokemon:")
type21=input("First type? (no caps): ")
type(type21)
type22=input("Second type? (no caps): ")
type(type22)
print("")

poke=dict[type11]+dict[type12]+dict[type21]+dict[type22]

for t in range(len(poke)):
    if poke[t]<0:
        poke[t]=-1
    elif poke[t]>0:
        poke[t]=1
    else: continue

A=np.column_stack(([normal,fighting,flying,poison,ground,rock,bug,ghost,steel,fire,water,grass,electric,psychic,ice,dragon,dark,fairy]))

weak=any(poke<0)
p=np.linspace(0,0,18)
if weak==True:
    for t in range(18):
        if poke[t]<0:
            p[t]=1
        else:
            p[t]=0
else:
    print("....your team has no weaknesses....")

q=[]
for t in range(len(p)):
    if p[t]==1:
        q.append(t)

for u in range(0,18):
    for v in range(u,18):
        combo=A[:,u]+A[:,v]
        for t in range(0,18):
            if combo[t]<0:
                combo[t]=-1
            elif combo[t]>0:
                combo[t]=1
            else: continue
        if len(q)==1:
            if combo[q[0]]==-poke[q[0]]:
                if u==v:
                    print(value[u])
                else:
                    print(value[u],value[v])
            else: continue
        if len(q)==2:
            if combo[q[0]]==-poke[q[0]] and combo[q[1]]==-poke[q[1]]:
                if u==v:
                    print(value[u])
                else:
                    print(value[u],value[v])
            else: continue
        elif len(q)==3:
            if combo[q[0]]==-poke[q[0]] and combo[q[1]]==-poke[q[1]] and combo[q[2]]==-poke[q[2]]:
                if u==v:
                    print(value[u])
                else:
                    print(value[u],value[v])
            else: continue
        elif len(q)>=4:
            break
        else: continue
while len(q)==3:
    if len(q)!=3:
        break
    print("If you didn't get any results, type 'ok' to get results for all two-pair combinations, otherwise type 'bye'")
    res=input("?:")
    if res=='bye':
        break
    if res=='ok':
        print('*without', value[q[2]])
        print('**without', value[q[0]])
        print('***without', value[q[1]])
        print("")
        for u in range(0,18):
            for v in range(u,18):
                combo=A[:,u]+A[:,v]
                for t in range(0,18):
                    if combo[t]<0:
                        combo[t]=-1
                    elif combo[t]>0:
                        combo[t]=1
                    else: continue
                if combo[q[0]]==-poke[q[0]] and combo[q[1]]==-poke[q[1]]:
                    if u==v:
                        print('*' + value[u])
                    else:
                        print('*' + value[u],value[v])
                elif combo[q[2]]==-poke[q[2]] and combo[q[1]]==-poke[q[1]]:
                    if u==v:
                        print('**' + value[u])
                    else:
                        print('**' + value[u],value[v])
                elif combo[q[0]]==-poke[q[0]] and combo[q[2]]==-poke[q[2]]:
                    if u==v:
                        print('***' + value[u])
                    else:
                        print('***' + value[u],value[v])
                else: continue
    else: break
        
while len(q)>=4:
    if len(q)<4:
        break
    else:
        print("")
        print("Your Pokemon are weak to:")
        print("")
        for s in range(len(q)):
            print(value[q[s]])
        print("")
        print("There may not be a Pokemon that meets every requirement.\n")
        print("Type 'continue' to see if that Pokemon exists, type 'ok' to try different combinations, or type 'bye' to exit\n")
        ans=str(input("?:"))
        if ans=='bye': break
        if ans=='continue':
            for u in range(0,18):
                for v in range(u,18):
                    combo=A[:,u]+A[:,v]
                    for t in range(0,18):
                        if combo[t]<0:
                            combo[t]=-1
                        elif combo[t]>0:
                            combo[t]=1
                        else: continue
                    if len(q)==4:
                        if combo[q[0]]==-poke[q[0]] and combo[q[1]]==-poke[q[1]] and combo[q[2]]==-poke[q[2]] and combo[q[3]]==-poke[q[3]]:
                            if u==v:
                                print(value[u])
                            else:
                                print(value[u],value[v])
                        else: continue
                    if len(q)==5:
                        if combo[q[0]]==-poke[q[0]] and combo[q[1]]==-poke[q[1]] and combo[q[2]]==-poke[q[2]] and combo[q[3]]==-poke[q[3]] and combo[q[4]]==-poke[q[4]]:
                            if u==v:
                                print(value[u])
                            else:
                                print(value[u],value[v])
                        else: continue
                    if len(q)==6:
                        if combo[q[0]]==-poke[q[0]] and combo[q[1]]==-poke[q[1]] and combo[q[2]]==-poke[q[2]] and combo[q[3]]==-poke[q[3]] and combo[q[4]]==-poke[q[4]] and combo[q[5]]==-poke[q[5]]:
                            if u==v:
                                print(value[u])
                            else:
                                print(value[u],value[v])
                        else: continue
                    if len(q)==7:
                        if combo[q[0]]==-poke[q[0]] and combo[q[1]]==-poke[q[1]] and combo[q[2]]==-poke[q[2]] and combo[q[3]]==-poke[q[3]] and combo[q[4]]==-poke[q[4]] and combo[q[5]]==-poke[q[5]] and combo[q[6]]==-poke[q[6]]:
                            if u==v:
                                print(value[u])
                            else:
                                print(value[u],value[v])
                        else: continue
                    if len(q)>=8:
                        print("Why do your Pokemon have so many weaknesses!! No!!!")
                        break
                        break
            print("")
            print("If you got an answer type 'bye', if you'd like to continue type 'ok'\n")
            bluh=str(input("?:"))
            if bluh=='bye':
                break
            if bluh=='ok':
                ans='ok'
        if ans=='ok':
            if len(q)==4:
                print("Pick three types: \n")
                test1=input("First: ")
                test2=input("Second: ")
                test3=input("Third: ")
                print("")
                t1=test[test1]; t2=test[test2]; t3=test[test3];
                for u in range(0,18):
                        for v in range(u,18):
                            combo=A[:,u]+A[:,v]
                            for t in range(0,18):
                                if combo[t]<0:
                                    combo[t]=-1
                                elif combo[t]>0:
                                    combo[t]=1
                                else: continue
                            if combo[t1]==-poke[t1] and combo[t2]==-poke[t2] and combo[t3]==-poke[t3]:
                                if u==v:
                                    print(value[u])
                                else:
                                    print(value[u],value[v])
                            else: continue
            if len(q)==5:
                x=input("How many types would you like to test? (3 or 4): ")
                print("")
                if x=='3':
                    test1=input("First: ")
                    test2=input("Second: ")
                    test3=input("Third: ")
                    print("")
                    t1=test[test1]; t2=test[test2]; t3=test[test3]
                    for u in range(0,18):
                        for v in range(u,18):
                            combo=A[:,u]+A[:,v]
                            for t in range(0,18):
                                if combo[t]<0:
                                    combo[t]=-1
                                elif combo[t]>0:
                                    combo[t]=1
                                else: continue
                            if combo[t1]==-poke[t1] and combo[t2]==-poke[t2] and combo[t3]==-poke[t3]:
                                if u==v:
                                    print(value[u])
                                else:
                                    print(value[u],value[v])
                            else: continue                   
                if x=='4':
                    test1=input("First: ")
                    test2=input("Second: ")
                    test3=input("Third: ")
                    test4=input("Fourth: ")
                    print("")
                    t1=test[test1]; t2=test[test2]; t3=test[test3]; t4=test[test4]
                    for u in range(0,18):
                        for v in range(u,18):
                            combo=A[:,u]+A[:,v]
                            for t in range(0,18):
                                if combo[t]<0:
                                    combo[t]=-1
                                elif combo[t]>0:
                                    combo[t]=1
                                else: continue
                            if combo[t1]==-poke[t1] and combo[t2]==-poke[t2] and combo[t3]==-poke[t3] and combo[t4]==-poke[t4]:
                                if u==v:
                                    print(value[u])
                                else:
                                    print(value[u],value[v])
                            else: continue  
            if len(q)==6:
                x=input("How many types would you like to test? (4 or 5): ")
                print("")
                if x=='4':
                    test1=input("First: ")
                    test2=input("Second: ")
                    test3=input("Third: ")
                    test4=input("Fourth: ")
                    print("")
                    t1=test[test1]; t2=test[test2]; t3=test[test3]; t4=test[test4]
                    for u in range(0,18):
                        for v in range(u,18):
                            combo=A[:,u]+A[:,v]
                            for t in range(0,18):
                                if combo[t]<0:
                                    combo[t]=-1
                                elif combo[t]>0:
                                    combo[t]=1
                                else: continue
                            if combo[t1]==-poke[t1] and combo[t2]==-poke[t2] and combo[t3]==-poke[t3] and combo[t4]==-poke[t4]:
                                if u==v:
                                    print(value[u])
                                else:
                                    print(value[u],value[v])
                            else: continue  
                if x=='5':
                    test1=input("First: ")
                    test2=input("Second: ")
                    test3=input("Third: ")
                    test4=input("Fourth: ")
                    test5=input("Fifth: ")
                    print("")
                    t1=test[test1]; t2=test[test2]; t3=test[test3]; t4=test[test4]; t5=test[test5]
                    for u in range(0,18):
                        for v in range(u,18):
                            combo=A[:,u]+A[:,v]
                            for t in range(0,18):
                                if combo[t]<0:
                                    combo[t]=-1
                                elif combo[t]>0:
                                    combo[t]=1
                                else: continue
                            if combo[t1]==-poke[t1] and combo[t2]==-poke[t2] and combo[t3]==-poke[t3] and combo[t4]==-poke[t4] and combo[t5]==-poke[t5]:
                                if u==v:
                                    print(value[u])
                                else:
                                    print(value[u],value[v])
                            else: continue  
            if len(q)==7:
                x=input("How many types would you like to test? (4, 5 or 6): ")
                print("")
                if x=='4':
                    test1=input("First: ")
                    test2=input("Second: ")
                    test3=input("Third: ")
                    test4=input("Fourth: ")
                    print("")
                    t1=test[test1]; t2=test[test2]; t3=test[test3]; t4=test[test4]
                    for u in range(0,18):
                        for v in range(u,18):
                            combo=A[:,u]+A[:,v]
                            for t in range(0,18):
                                if combo[t]<0:
                                    combo[t]=-1
                                elif combo[t]>0:
                                    combo[t]=1
                                else: continue
                            if combo[t1]==-poke[t1] and combo[t2]==-poke[t2] and combo[t3]==-poke[t3] and combo[t4]==-poke[t4]:
                                if u==v:
                                    print(value[u])
                                else:
                                    print(value[u],value[v])
                            else: continue  
                if x=='5':
                    test1=input("First: ")
                    test2=input("Second: ")
                    test3=input("Third: ")
                    test4=input("Fourth: ")
                    test5=input("Fifth: ")
                    print("")
                    t1=test[test1]; t2=test[test2]; t3=test[test3]; t4=test[test4]; t5=test[test5]
                    for u in range(0,18):
                        for v in range(u,18):
                            combo=A[:,u]+A[:,v]
                            for t in range(0,18):
                                if combo[t]<0:
                                    combo[t]=-1
                                elif combo[t]>0:
                                    combo[t]=1
                                else: continue
                            if combo[t1]==-poke[t1] and combo[t2]==-poke[t2] and combo[t3]==-poke[t3] and combo[t4]==-poke[t4] and combo[t5]==-poke[t5]:
                                if u==v:
                                    print(value[u])
                                else:
                                    print(value[u],value[v])
                            else: continue  
                if x=='6':
                    test1=input("First: ")
                    test2=input("Second: ")
                    test3=input("Third: ")
                    test4=input("Fourth: ")
                    test5=input("Fifth: ")
                    test6=input("Sixth: ")
                    print("")
                    t1=test[test1]; t2=test[test2]; t3=test[test3]; t4=test[test4]; t5=test[test5]; t6=test[test6]
                    for u in range(0,18):
                        for v in range(u,18):
                            combo=A[:,u]+A[:,v]
                            for t in range(0,18):
                                if combo[t]<0:
                                    combo[t]=-1
                                elif combo[t]>0:
                                    combo[t]=1
                                else: continue
                            if combo[t1]==-poke[t1] and combo[t2]==-poke[t2] and combo[t3]==-poke[t3] and combo[t4]==-poke[t4] and combo[t5]==-poke[t5] and combo[t6]==-poke[t6]:
                                if u==v:
                                    print(value[u])
                                else:
                                    print(value[u],value[v])
                            else: continue  
            if len(q)>=8:
                print("You have too many weaknesses!! No!!!")
                break
