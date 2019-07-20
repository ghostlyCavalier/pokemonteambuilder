import numpy as np
import sys
import tkinter
from tkinter import Menu,Frame,Label,Button,Tk,IntVar,StringVar,Checkbutton,OptionMenu,Toplevel,Scrollbar
from tkinter.filedialog import asksaveasfile

class GUI:
    def __init__(self):
        self.window=Tk()
        self.window.title('Battle Tree Builder')
        
        #Strength Arrays
        self.nor=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.fig=np.array([1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0])
        self.fly=np.array([0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0])
        self.poi=np.array([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1])
        self.gro=np.array([0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,0])
        self.roc=np.array([0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0])
        self.buu=np.array([0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0])
        self.gho=np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0])
        self.ste=np.array([0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1])
        self.fir=np.array([0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0])
        self.wat=np.array([0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0])
        self.gra=np.array([0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0])
        self.ele=np.array([0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
        self.psy=np.array([0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.icc=np.array([0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0])
        self.dra=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
        self.dar=np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0])
        self.fai=np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0])
        
        #Weak Arrays + Strength Arrays
        self.normal=np.array([0,-1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]) + self.nor
        self.fighting=np.array([0,0,-1,0,0,1,1,0,0,0,0,0,0,-1,0,0,1,-1]) + self.fig
        self.flying=np.array([0,1,0,0,1,-1,1,0,0,0,0,1,-1,0,-1,0,0,0]) + self.fly
        self.poison=np.array([0,1,0,1,-1,0,1,0,0,0,0,1,0,-1,0,0,0,1]) + self.poi
        self.ground=np.array([0,0,0,1,0,1,0,0,0,0,-1,-1,1,0,-1,0,0,0]) + self.gro
        self.rock=np.array([1,-1,1,1,-1,0,0,0,-1,1,-1,-1,0,0,0,0,0,0]) + self.roc
        self.bug=np.array([0,1,-1,0,1,-1,0,0,0,-1,0,1,0,0,0,0,0,0]) + self.buu
        self.ghost=np.array([1,1,0,1,0,0,1,-1,0,0,0,0,0,0,0,0,-1,0]) + self.gho
        self.steel=np.array([1,-1,1,1,-1,1,1,0,1,-1,0,1,0,1,1,1,0,1]) + self.ste
        self.fire=np.array([0,0,0,0,-1,-1,1,0,1,1,-1,1,0,0,1,0,0,1]) + self.fir
        self.water=np.array([0,0,0,0,0,0,0,0,1,1,1,-1,-1,0,1,0,0,0]) + self.wat
        self.grass=np.array([0,0,-1,-1,1,0,-1,0,0,-1,1,1,1,0,-1,0,0,0]) + self.gra
        self.electric=np.array([0,0,1,0,-1,0,0,0,1,0,0,0,1,0,0,0,0,0]) + self.ele
        self.psychic=np.array([0,1,0,0,0,0,-1,-1,0,0,0,0,0,1,0,0,-1,0]) + self.psy
        self.ice=np.array([0,-1,0,0,0,-1,0,0,-1,-1,0,0,0,0,1,0,0,0]) + self.icc
        self.dragon=np.array([0,0,0,0,0,0,0,0,0,1,1,1,1,0,-1,-1,0,-1]) + self.dra
        self.dark=np.array([0,-1,0,0,0,0,-1,1,0,0,0,0,0,1,0,0,1,-1]) + self.dar
        self.fairy=np.array([0,1,0,-1,0,0,1,0,-1,0,0,0,0,0,0,1,1,0]) + self.fai
        self.none=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

        self.A=np.column_stack(([self.normal,self.fighting,self.flying,self.poison,self.ground,
                                 self.rock,self.bug,self.ghost,self.steel,self.fire,self.water,
                                 self.grass,self.electric,self.psychic,self.ice,self.dragon,self.dark,
                                 self.fairy]))

        frame1=Frame(self.window)
        frame2=Frame(self.window)
        frame3=Frame(self.window)
        self.frame4=Frame(self.window)

        Label(frame1,text='Welcome to the Battle Tree Builder v1.0!').grid(row=0)
        Label(frame1,text='Please pick the typing of your two Pokemon:\n').grid(row=1)

        #Dropdown with options for picking types
        Label(frame2,text='First Pokemon:').grid(column=0,row=2)
        self.type11 = tkinter.StringVar(frame2)
        self.type11.set('none')
        self.w11=OptionMenu(frame2,self.type11,'none','normal','fighting','flying','poison',
                            'ground','rock','bug','ghost','steel','fire','water','grass','electric','psychic',
                            'ice','dragon','dark','fairy').grid(column=0,row=3)

        self.type12 = tkinter.StringVar(frame2)
        self.type12.set('none')
        self.w12=OptionMenu(frame2,self.type12,'none','normal','fighting','flying','poison',
                            'ground','rock','bug','ghost','steel','fire','water','grass','electric','psychic',
                            'ice','dragon','dark','fairy').grid(column=0,row=4)

        Label(frame2,text='Second Pokemon:').grid(column=1,row=2)
        self.type21 = tkinter.StringVar(frame3)
        self.type21.set('none')
        self.w21=OptionMenu(frame2,self.type21,'none','normal','fighting','flying','poison',
                            'ground','rock','bug','ghost','steel','fire','water','grass','electric','psychic',
                            'ice','dragon','dark','fairy').grid(column=1,row=3)

        self.type22 = tkinter.StringVar(frame3)
        self.type22.set('none')
        self.w22=OptionMenu(frame2,self.type22,'none','normal','fighting','flying','poison',
                            'ground','rock','bug','ghost','steel','fire','water','grass','electric','psychic',
                            'ice','dragon','dark','fairy').grid(column=1,row=4)

        Button(frame3,text='Okay',command=self.clear).pack()

        frame1.grid()
        frame2.grid()
        frame3.grid()
        self.frame4.grid()

        tkinter.mainloop()
        
    def clear(self):
        self.frame4.destroy()
        self.checkbox()
        
    def checkbox(self):
        self.frame4=Frame(self.window)
        self.frame4.grid()
  
        self.pika={}
        self.pika["normal"]=np.array([0,-1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
        self.pika["fighting"]=np.array([0,0,-1,0,0,1,1,0,0,0,0,0,0,-1,0,0,1,-1,0])
        self.pika["flying"]=np.array([0,1,0,0,2,-1,1,0,0,0,0,1,-1,0,-1,0,0,0,0])
        self.pika["poison"]=np.array([0,1,0,1,-1,0,1,0,0,0,0,1,0,-1,0,0,0,1,0])
        self.pika["ground"]=np.array([0,0,0,1,0,1,0,0,0,0,-1,-1,1,0,-1,0,0,0,0])
        self.pika["rock"]=np.array([1,-1,1,1,-1,0,0,0,-1,1,-1,-1,0,0,0,0,0,0,0])
        self.pika["bug"]=np.array([0,1,-1,0,1,-1,0,0,0,-1,0,1,0,0,0,0,0,0,0])
        self.pika["ghost"]=np.array([2,1,0,1,0,0,1,-1,0,0,0,0,0,0,0,0,-1,0,0])
        self.pika["steel"]=np.array([1,-1,1,2,-1,1,1,0,1,-1,0,1,0,1,1,1,0,1,0])
        self.pika["fire"]=np.array([0,0,0,0,-1,-1,1,0,1,1,-1,1,0,0,1,0,0,1,0])
        self.pika["water"]=np.array([0,0,0,0,0,0,0,0,1,1,1,-1,-1,0,1,0,0,0,0])
        self.pika["grass"]=np.array([0,0,-1,-1,1,0,-1,0,0,-1,1,1,1,0,-1,0,0,0,0])
        self.pika["electric"]=np.array([0,0,1,0,-1,0,0,0,1,0,0,0,1,0,0,0,0,0,0])
        self.pika["psychic"]=np.array([0,1,0,0,0,0,-1,-1,0,0,0,0,0,1,0,0,-1,0,0])
        self.pika["ice"]=np.array([0,-1,0,0,0,-1,0,0,-1,-1,0,0,0,0,1,0,0,0,0])
        self.pika["dragon"]=np.array([0,0,0,0,0,0,0,0,0,1,1,1,1,0,-1,-1,0,-1,0])
        self.pika["dark"]=np.array([0,-1,0,0,0,0,-1,1,0,0,0,0,0,2,0,0,1,-1,0])
        self.pika["fairy"]=np.array([0,1,0,-1,0,0,1,0,-1,0,0,0,0,0,0,2,1,0,0])
        self.pika["none"]=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

        self.value={}
        self.value[0]="Normal"
        self.value[1]="Fighting"
        self.value[2]="Flying"
        self.value[3]="Poison"
        self.value[4]="Ground"
        self.value[5]="Rock"
        self.value[6]="Bug"
        self.value[7]="Ghost"
        self.value[8]="Steel"
        self.value[9]="Fire"
        self.value[10]="Water"
        self.value[11]="Grass"
        self.value[12]="Electric"
        self.value[13]="Psychic"
        self.value[14]="Ice"
        self.value[15]="Dragon"
        self.value[16]="Dark"
        self.value[17]="Fairy"
        
        self.poke=self.pika[self.type11.get()]+self.pika[self.type12.get()]+self.pika[self.type21.get()]+self.pika[self.type22.get()]

        for t in range(len(self.poke)):
            if self.poke[t]<0:
                self.poke[t]=-1
            elif self.poke[t]>0:
                self.poke[t]=1
            else: continue

        #Identify what the Pokemon are weak to
        weak=any(self.poke<0)
        p=np.linspace(0,0,len(self.poke))
        if weak==True:
            for t in range(len(self.poke)):
                if self.poke[t]<0:
                    p[t]=1
                else:
                    p[t]=0
        elif self.type11.get()=='none' and self.type12.get()=='none' and self.type21.get()=='none' and self.type22.get()=='none':
            Label(self.frame4,text="bitch").grid()
        else:
            Label(self.frame4,text="....your team has no weaknesses....").grid()

        self.q=[]
        for t in range(len(p)):
            if p[t]==1:
                self.q.append(t)
            else: continue
        #print(p,self.q)

        
        #GUI stuff
        #For 1 weakness

        self.cb=[]
        self.cbv=[]

        for t in range(0,len(self.q)):
            self.cbv.append('')
            self.cbv[t]=IntVar()
            self.cbv[t].set(1)
        for t in range(0,len(self.q)):
            self.cb.append(Checkbutton(self.frame4,text=str(self.value[self.q[t]]),variable=self.cbv[t]))
        for t in range(0,len(self.q)):
            self.cb[t].grid()            
        if weak==True:
            Button(self.frame4,text='Okay',command=self.results).grid()

        
    def results(self):
        #Checks over all possible combinations
        self.win=Toplevel(master=self.window, height=500,width=500)
        self.win.title('Results')
        scroll=Scrollbar(self.win)
        scroll.pack(side='right',fill='y')
        self.listbox=tkinter.Listbox(self.win,width=25)
        self.listbox.config(yscrollcommand=scroll.set)
        scroll.config(command=self.listbox.yview)
        for u in range(0,18):
            for v in range(u,18):
                self.combo=self.A[:,u]+self.A[:,v]
                for t in range(0,18):
                    if self.combo[t]<0:
                        self.combo[t]=-1
                    elif self.combo[t]>0:
                        self.combo[t]=1
                    else: continue
                bin=''
                for t in range(0,len(self.q)):
                    if t==0:
                        bin+='[self.cbv['+str(t)+'].get()'
                    elif t <= (len(self.q)-1):
                        bin+=',self.cbv['+str(t)+'].get()'
                    if t==len(self.q)-1:
                        bin+=']'
                bin=eval(bin)
                h=[] #h the array containing the indices of q corresponding to which boxes are checked
                for t in range(len(bin)):
                    if bin[t]==1:
                        h.append(t)
                    else: continue
                cond=''
                for t in range(0,len(h)):
                    cond+='self.combo[self.q[h['+str(t)+']]]==-self.poke[self.q[h['+str(t)+']]]'
                    if t < (len(h)-1):
                        cond+=' and '
                if eval(cond):
                    if u==v:
                        self.listbox.insert(1,self.value[u])
                    else:
                        self.listbox.insert(1,self.value[u] + " " + self.value[v])
        self.listbox.insert(tkinter.END,' ')                    
        self.listbox.insert(tkinter.END,'End of Results')
        self.listbox.pack()
        self.menu()
    def menu(self):
        menubar=Menu(self.win)
        file=Menu(menubar,tearoff=0)
        file.add_command(label='Save Results',command=self.save)
        file.add_command(label='Exit',command=self.win.destroy)
        menubar.add_cascade(label='File',menu=file)
        self.win.config(menu=menubar)
    def save(self):
        global filename
        f=asksaveasfile(mode='w',defaultextension='.txt')
        results=self.listbox.get(0,tkinter.END)
        try:
            f.write('Working Team:\n')
            f.write(self.type11.get().capitalize() + ' ' + self.type12.get().capitalize() +'\n')
            f.write(self.type21.get().capitalize() + ' ' + self.type22.get().capitalize() +'\n\n')
            f.write('Possible Friends:\n')
            for t in range(0,self.listbox.size()-1):
                f.write(results[t]+'\n')
            f.close()
        except:
            return
                        
                    
GUI()



        
