from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from pyodbc import*



base=connect("Driver={SQL Server Native Client 11.0};Server=DESKTOP-H27UPSP\SQLEXPRESS01;Database=AUTO_CLEAN;Trusted_Connection=yes;")
cr=base.cursor()
c1='#abcdef'
c2='#ddddee'
c3='#ddddcc'
c4='#345678'

atw=0
wid,heg,tk,nwl,clb,crb,zkb,wrb,inb=0,0,0,0,0,0,0,0,0

def main():
    global tk,wid,heg,nwl,clb,crb,zkb,wrb,inb

    if tk!=0:
        tk.destroy()
    
    tk=Tk()
    
    if wid==0 and heg==0:
        wid=tk.winfo_screenwidth()
        heg=tk.winfo_screenheight()
        
    tk.geometry('%dx%d+%d+%d'%(wid//4.5,heg//2,(wid-wid//4.5)//2,(heg-heg//2)//2))
    
    if atw==0:
        
        nwl=Label(tk,text='Необходима авторизация',font='Arial 24',bg=c1)
        nwl.pack()
        nwl.place(relx=0,rely=0,relheight=1/6,relwidth=1)

        clb=Button(tk,text='Клиенты',font='Arial 24',bg=c2,command=author)
        clb.pack()
        clb.place(relx=0,rely=1/6,relheight=1/6,relwidth=1)

        crb=Button(tk,text='Автомобили',font='Arial 24',bg=c1,command=author)
        crb.pack()
        crb.place(relx=0,rely=2/6,relheight=1/6,relwidth=1)

        zkb=Button(tk,text='Текущие заказы',font='Arial 24',bg=c2,command=author)
        zkb.pack()
        zkb.place(relx=0,rely=3/6,relheight=1/6,relwidth=1)

        wrb=Button(tk,text='Работники',font='Arial 24',bg=c1,command=author)
        wrb.pack()
        wrb.place(relx=0,rely=4/6,relheight=1/6,relwidth=1)

        inb=Button(tk,text='О программе',font='Arial 24',bg=c2,command=author)
        inb.pack()
        inb.place(relx=0,rely=5/6,relheight=1/6,relwidth=1)

    else:

        nwl=Label(tk,text='Добро пожаловать!',font='Arial 24',bg=c1)
        nwl.pack()
        nwl.place(relx=0,rely=0,relheight=1/6,relwidth=1)

        clb=Button(tk,text='Клиенты',font='Arial 24',bg=c2,command=clw)
        clb.pack()
        clb.place(relx=0,rely=1/6,relheight=1/6,relwidth=1)

        crb=Button(tk,text='Автомобили',font='Arial 24',bg=c1,command=crw)
        crb.pack()
        crb.place(relx=0,rely=2/6,relheight=1/6,relwidth=1)

        zkb=Button(tk,text='Текущие заказы',font='Arial 24',bg=c2,command=zkw)
        zkb.pack()
        zkb.place(relx=0,rely=3/6,relheight=1/6,relwidth=1)

        wrb=Button(tk,text='Работники',font='Arial 24',bg=c1,command=wrw)
        wrb.pack()
        wrb.place(relx=0,rely=4/6,relheight=1/6,relwidth=1)

        inb=Button(tk,text='О программе',font='Arial 24',bg=c2,command=print)
        inb.pack()
        inb.place(relx=0,rely=5/6,relheight=1/6,relwidth=1)

def author():
    global atw,nwl,clb,crb,zkb,wrb,inb,tk
    if not atw in[0,1]:
        atw.destroy()
    atw=Tk()
    atw.wm_attributes("-topmost", 2)
    atw.geometry('%dx%d+%d+%d'%(wid//4,heg//3,(wid-wid//4)//2,(heg-heg//3)//2))
    Label(atw,text='Авторизация',font='Arial 24',bg=c1).place(relx=0,rely=0,relheight=1/4,relwidth=1)
    
    atl=Entry(atw,font='Arial 24',justify='center',bg=c2)
    atl.pack()
    atl.place(relx=0,rely=1/4,relwidth=1,relheight=1/4)
    atl.insert(0,'Логин')

    atp=Entry(atw,font='Arial 24',justify='center',bg=c1)
    atp.pack()
    atp.place(relx=0,rely=2/4,relwidth=1,relheight=1/4)
    atp.insert(0,'Пароль')

    def ain():
        global atw
        if atl.get()=='root' and atp.get()=='12345':
            clb['command']=clw
            crb['command']=crw
            zkb['command']=zkw
            wrb['command']=wrw
            inb['command']=print
            nwl['text']='Добро пожаловать!'
            atw.destroy()
            atw=1
            tk.wm_attributes("-topmost", 2)
    
    ati=Button(atw,text='Bойти',font='Arial 24',bg=c2,command=ain)
    ati.pack()
    ati.place(relx=0,rely=3/4,relwidth=1,relheight=1/4)

def clw():
    global tk
    tk.destroy()
    tk=Tk()
    tk.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

    cla=Button(tk,text='Добавить',font='Arial 24',bg=c2,command=cln)
    cla.pack()
    cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)

    def cha():
        global tk
        ti=int(table.focus()[1:])-1
        zn=[e for e in cr.execute('SELECT * FROM CLIENT')]
        dn=[e[1:-1]for e in zn]
        tid=str(zn[ti][0])

        tk.destroy()
        tk=Tk()
        tk.geometry('%dx%d+%d+%d'%(wid*0.8,heg*0.3,(wid-wid*0.8)//2,(heg-heg*0.3)//2))

        bt=['Имя','Фамилия','Отчество','Номер телефона']
        v=[0 for i in range(len(bt))]
        
        for i in range(len(bt)):
            Label(tk,text=bt[i],font='Arial 16',bg=c1).place(relx=i/len(bt),rely=0,relheight=1/3,relwidth=1/len(bt))
            v[i]=Entry(tk,font='Arial 14',justify='center',bg=c2)
            v[i].pack()
            v[i].place(relx=i/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))
            v[i].insert(0,str(dn[ti][i]))

        def add():
            co=("UPDATE CLIENT SET NAME='%s',VORNAME='%s',LASTNAME='%s',NUMBER='%s' WHERE CLIENT_ID="+tid)%tuple(v[i].get()for i in range(len(v)))
            cr.execute(co)
            cr.commit()
            clw()
        
        Label(tk,bg=c1).place(rely=2/3,relx=0,relwidth=1,relheight=1/3)
        Button(tk,text='Изменить',font='Arial 24',bg=c1,command=add).place(relx=0.35,rely=2/3,relwidth=0.15,relheight=1/3)
        Button(tk,text='Отмена',font='Arial 24',bg=c1,command=clw).place(relx=0.5,rely=2/3,relwidth=0.15,relheight=1/3)

    clr=Button(tk,text='Изменить',font='Arial 24',bg=c2,command=cha)
    clr.pack()
    clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

    def rem():
        ti=int(table.focus()[1:])-1
        zn=[e for e in cr.execute('SELECT * FROM CLIENT')]
        cr.execute('DELETE FROM CLIENT WHERE CLIENT_ID='+str(zn[ti][0]))
        cr.commit()
        clw()
    
    cld=Button(tk,text='Удалить',font='Arial 24',bg=c2,command=rem)
    cld.pack()
    cld.place(relx=0.8,rely=2/8,relwidth=0.2,relheight=1/8)

    mnb=Button(tk,text='К главному',font='Arial 24',bg=c2,command=main)
    mnb.pack()
    mnb.place(relx=0.8,rely=7/8,relwidth=0.2,relheight=1/8)

    dn=[e[1:-1]for e in cr.execute('SELECT * FROM CLIENT')]
    
    bt=['Имя','Фамилия','Отчество','Номер телефона']

    st=ttk.Style()
    st.theme_use("clam")
    st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
    st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
    st.map("Treeview",background=[("selected",c4)])

    table=ttk.Treeview(tk,show="headings",columns=tuple(e for e in'0123'),style="mystyle.Treeview")

    for i in range(len(bt)):
        table.heading(str(i),text=bt[i])

    for e in dn:
        table.insert('',END,values=tuple(e))

    table.pack()
    table.place(relx=0,rely=0,relwidth=0.8,relheight=1)

def cln():
    global tk
    tk.destroy()
    tk=Tk()
    tk.geometry('%dx%d+%d+%d'%(wid*0.8,heg*0.3,(wid-wid*0.8)//2,(heg-heg*0.3)//2))

    bt=['Имя','Фамилия','Отчество','Номер телефона']
    v=[0 for i in range(len(bt))]
    
    for i in range(len(bt)):
        Label(tk,text=bt[i],font='Arial 16',bg=c1).place(relx=i/len(bt),rely=0,relheight=1/3,relwidth=1/len(bt))
        v[i]=Entry(tk,font='Arial 14',justify='center',bg=c2)
        v[i].pack()
        v[i].place(relx=i/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

    def add():
        co="INSERT INTO CLIENT (NAME,VORNAME,LASTNAME,NUMBER) VALUES ('%s','%s','%s','%s')"%tuple(v[i].get()for i in range(len(v)))
        cr.execute(co)
        cr.commit()
        clw()
    
    Label(tk,bg=c1).place(rely=2/3,relx=0,relwidth=1,relheight=1/3)
    Button(tk,text='Добавить',font='Arial 24',bg=c1,command=add).place(relx=0.35,rely=2/3,relwidth=0.15,relheight=1/3)
    Button(tk,text='Отмена',font='Arial 24',bg=c1,command=clw).place(relx=0.5,rely=2/3,relwidth=0.15,relheight=1/3)

def crw():
    global tk
    tk.destroy()
    tk=Tk()
    tk.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

    cla=Button(tk,text='Добавить',font='Arial 24',bg=c2,command=cra)
    cla.pack()
    cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)

    def cha():
        global tk
        ti=int(table.focus()[1:])-1
        zn=[e for e in cr.execute('SELECT * FROM CAR')]
        dn=[e[1:-1]for e in zn]
        tid=str(zn[ti][0])

        tk.destroy()
        tk=Tk()
        tk.geometry('%dx%d+%d+%d'%(wid*0.8,heg*0.3,(wid-wid*0.8)//2,(heg-heg*0.3)//2))

        bt=['Марка','Длина','Ширина','Номер','Цвет']
        v=[0 for i in range(len(bt))]
        
        for i in range(len(bt)):
            Label(tk,text=bt[i],font='Arial 16',bg=c1).place(relx=i/len(bt),rely=0,relheight=1/3,relwidth=1/len(bt))
            v[i]=Entry(tk,font='Arial 14',justify='center',bg=c2)
            v[i].pack()
            v[i].place(relx=i/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))
            v[i].insert(0,str(dn[ti][i]))

        def add():
            co=("UPDATE CAR SET MARK='%s',WIDTH=%s,HEIGHT=%s,NUMBER='%s',COLOR='%s' WHERE CAR_ID="+tid)%tuple(v[i].get()for i in range(len(v)))
            cr.execute(co)
            cr.commit()
            crw()
        
        Label(tk,bg=c1).place(rely=2/3,relx=0,relwidth=1,relheight=1/3)
        Button(tk,text='Изменить',font='Arial 24',bg=c1,command=add).place(relx=0.35,rely=2/3,relwidth=0.15,relheight=1/3)
        Button(tk,text='Отмена',font='Arial 24',bg=c1,command=crw).place(relx=0.5,rely=2/3,relwidth=0.15,relheight=1/3)
    
    clr=Button(tk,text='Изменить',font='Arial 24',bg=c2,command=cha)
    clr.pack()
    clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

    def rem():
        ti=int(table.focus()[1:])-1
        zn=[e for e in cr.execute('SELECT * FROM CAR')]
        cr.execute('DELETE FROM CAR WHERE CAR_ID='+str(zn[ti][0]))
        cr.commit()
        crw()
    
    cld=Button(tk,text='Удалить',font='Arial 24',bg=c2,command=rem)
    cld.pack()
    cld.place(relx=0.8,rely=2/8,relwidth=0.2,relheight=1/8)

    mnb=Button(tk,text='К главному',font='Arial 24',bg=c2,command=main)
    mnb.pack()
    mnb.place(relx=0.8,rely=7/8,relwidth=0.2,relheight=1/8)

    dn=[e[1:-1]for e in cr.execute('SELECT * FROM CAR')]
    
    bt=['Марка','Длина','Ширина','Номер','Цвет']

    st=ttk.Style()
    st.theme_use("clam")
    st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
    st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
    st.map("Treeview",background=[("selected",c4)])

    table=ttk.Treeview(tk,show="headings",columns=tuple(e for e in'01234'),style="mystyle.Treeview")

    for i in range(len(bt)):
        table.heading(str(i),text=bt[i])

    for e in dn:
        table.insert('',END,values=tuple(e))

    table.pack()
    table.place(relx=0,rely=0,relwidth=0.8,relheight=1)

def cra():
    global tk
    tk.destroy()
    tk=Tk()
    tk.geometry('%dx%d+%d+%d'%(wid*0.8,heg*0.3,(wid-wid*0.8)//2,(heg-heg*0.3)//2))

    bt=['Марка','Длина','Ширина','Номер','Цвет']
    v=[0 for i in range(len(bt))]
    
    for i in range(len(bt)):
        Label(tk,text=bt[i],font='Arial 16',bg=c1).place(relx=i/len(bt),rely=0,relheight=1/3,relwidth=1/len(bt))
        v[i]=Entry(tk,font='Arial 14',justify='center',bg=c2)
        v[i].pack()
        v[i].place(relx=i/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

    def add():
        co="INSERT INTO CAR (MARK,WIDTH,HEIGHT,NUMBER,COLOR) VALUES ('%s',%s,%s,'%s','%s')"%tuple(v[i].get()for i in range(len(v)))
        cr.execute(co)
        cr.commit()
        crw()
    
    Label(tk,bg=c1).place(rely=2/3,relx=0,relwidth=1,relheight=1/3)
    Button(tk,text='Добавить',font='Arial 24',bg=c1,command=add).place(relx=0.35,rely=2/3,relwidth=0.15,relheight=1/3)
    Button(tk,text='Отмена',font='Arial 24',bg=c1,command=crw).place(relx=0.5,rely=2/3,relwidth=0.15,relheight=1/3)

def wrw():
    global tk
    tk.destroy()
    tk=Tk()
    tk.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

    cla=Button(tk,text='Добавить',font='Arial 24',bg=c2,command=wra)
    cla.pack()
    cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)

    def cha():
        global tk
        ti=int(table.focus()[1:])-1
        zn=[e for e in cr.execute('SELECT * FROM WORKER')]
        dn=[e[1:-1]for e in zn]
        tid=str(zn[ti][0])

        tk.destroy()
        tk=Tk()
        tk.geometry('%dx%d+%d+%d'%(wid*0.8,heg*0.3,(wid-wid*0.8)//2,(heg-heg*0.3)//2))

        bt=bt=['Имя','Фамилия','Отчество','Номер телефона','Опыт работы','Тип работы','Рабочее время']
        v=[0 for i in range(len(bt))]
        
        for i in range(len(bt)):
            Label(tk,text=bt[i],font='Arial 16',bg=c1).place(relx=i/len(bt),rely=0,relheight=1/3,relwidth=1/len(bt))
            v[i]=Entry(tk,font='Arial 14',justify='center',bg=c2)
            v[i].pack()
            v[i].place(relx=i/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))
            v[i].insert(0,str(dn[ti][i]))

        def add():
            co=("UPDATE WORKER SET NAME='%s',VORNAME='%s',LASTNAME='%s',NUMBER='%s',EXPER=%s,WORK='%s',WORKTIME='%s' WHERE WORKER_ID="+tid)%tuple(v[i].get()for i in range(len(v)))
            cr.execute(co)
            cr.commit()
            wrw()
        
        Label(tk,bg=c1).place(rely=2/3,relx=0,relwidth=1,relheight=1/3)
        Button(tk,text='Изменить',font='Arial 24',bg=c1,command=add).place(relx=0.35,rely=2/3,relwidth=0.15,relheight=1/3)
        Button(tk,text='Отмена',font='Arial 24',bg=c1,command=wrw).place(relx=0.5,rely=2/3,relwidth=0.15,relheight=1/3)

    
    clr=Button(tk,text='Изменить',font='Arial 24',bg=c2,command=cha)
    clr.pack()
    clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

    def rem():
        ti=int(table.focus()[1:])-1
        zn=[e for e in cr.execute('SELECT * FROM WORKER')]
        cr.execute('DELETE FROM WORKER WHERE WORKER_ID='+str(zn[ti][0]))
        cr.commit()
        wrw()
    
    cld=Button(tk,text='Удалить',font='Arial 24',bg=c2,command=rem)
    cld.pack()
    cld.place(relx=0.8,rely=2/8,relwidth=0.2,relheight=1/8)

    mnb=Button(tk,text='К главному',font='Arial 24',bg=c2,command=main)
    mnb.pack()
    mnb.place(relx=0.8,rely=7/8,relwidth=0.2,relheight=1/8)

    dn=[e[1:-1]for e in cr.execute('SELECT * FROM WORKER')]
    
    bt=['Имя','Фамилия','Отчество','Номер телефона','Опыт работы','Тип работы','Рабочее время']

    st=ttk.Style()
    st.theme_use("clam")
    st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
    st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
    st.map("Treeview",background=[("selected",c4)])

    table=ttk.Treeview(tk,show="headings",columns=tuple(e for e in'0123456'),style="mystyle.Treeview")

    for i in range(len(bt)):
        table.heading(str(i),text=bt[i])

    for e in dn:
        table.insert('',END,values=tuple(e))

    table.pack()
    table.place(relx=0,rely=0,relwidth=0.8,relheight=1)

def wra():
    global tk
    tk.destroy()
    tk=Tk()
    tk.geometry('%dx%d+%d+%d'%(wid*0.8,heg*0.3,(wid-wid*0.8)//2,(heg-heg*0.3)//2))

    bt=['Имя','Фамилия','Отчество','Номер телефона','Опыт работы','Тип работы','Рабочее время']
    v=[0 for i in range(len(bt))]
    
    for i in range(len(bt)):
        Label(tk,text=bt[i],font='Arial 16',bg=c1).place(relx=i/len(bt),rely=0,relheight=1/3,relwidth=1/len(bt))
        v[i]=Entry(tk,font='Arial 14',justify='center',bg=c2)
        v[i].pack()
        v[i].place(relx=i/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

    def add():
        co="INSERT INTO WORKER (NAME,VORNAME,LASTNAME,NUMBER,EXPER,WORK,WORKTIME) VALUES ('%s','%s','%s','%s',%s,'%s','%s')"%tuple(v[i].get()for i in range(len(v)))
        cr.execute(co)
        cr.commit()
        wrw()
    
    Label(tk,bg=c1).place(rely=2/3,relx=0,relwidth=1,relheight=1/3)
    Button(tk,text='Добавить',font='Arial 24',bg=c1,command=add).place(relx=0.35,rely=2/3,relwidth=0.15,relheight=1/3)
    Button(tk,text='Отмена',font='Arial 24',bg=c1,command=wrw).place(relx=0.5,rely=2/3,relwidth=0.15,relheight=1/3)

def zkw():
    global tk
    tk.destroy()
    tk=Tk()
    tk.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

    cla=Button(tk,text='Добавить',font='Arial 24',bg=c2,command=zka)
    cla.pack()
    cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)

    def cha():
        global tk
        ti=int(table.focus()[1:])-1
        zn=[e for e in cr.execute('SELECT * FROM LIST')]
        dn=[e[1:-1]for e in zn]
        tid=str(zn[ti][0])

        tk.destroy()
        tk=Tk()
        tk.geometry('%dx%d+%d+%d'%(wid*0.8,heg*0.3,(wid-wid*0.8)//2,(heg-heg*0.3)//2))

        bt=['Дата','Клиент','Работник','Автомобиль','Вид работы','Цена']
        
        for i in range(len(bt)):
            Label(tk,text=bt[i],font='Arial 16',bg=c1).place(relx=i/len(bt),rely=0,relheight=1/3,relwidth=1/len(bt))
        ddt=Entry(tk,font='Arial 14',justify='center',bg=c2)
        ddt.pack()
        ddt.place(relx=0,rely=1/3,relheight=1/3,relwidth=1/len(bt))

        def cle():
            te=Tk()
            te.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

            def enter():
                ti=int(table.focus()[1:])-1
                zn=[e for e in cr.execute('SELECT * FROM CLIENT')]
                dcl['text']=str(zn[ti][0])
                te.destroy()
            
            cla=Button(te,text='Выбрать',font='Arial 24',bg=c2,command=enter)
            cla.pack()
            cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)

            clr=Button(te,text='Отмена',font='Arial 24',bg=c2,command=(lambda:te.destroy()))
            clr.pack()
            clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

            dn=[e[1:-1]for e in cr.execute('SELECT * FROM CLIENT')]
            
            bt=['Имя','Фамилия','Отчество','Номер телефона']

            st=ttk.Style()
            st.theme_use("clam")
            st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
            st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
            st.map("Treeview",background=[("selected",c4)])

            table=ttk.Treeview(te,show="headings",columns=tuple(e for e in'0123'),style="mystyle.Treeview")

            for i in range(len(bt)):
                table.heading(str(i),text=bt[i])

            for e in dn:
                table.insert('',END,values=tuple(e))

            table.pack()
            table.place(relx=0,rely=0,relwidth=0.8,relheight=1)

        dcl=Button(tk,text='Выбрать\nклиента',font='Arial 14',bg=c2,command=cle)
        dcl.pack()
        dcl.place(relx=1/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

        def wre():
            te=Tk()
            te.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

            def enter():
                ti=int(table.focus()[1:])-1
                zn=[e for e in cr.execute('SELECT * FROM WORKER')]
                dwr['text']=str(zn[ti][0])
                te.destroy()

            cla=Button(te,text='Выбрать',font='Arial 24',bg=c2,command=enter)
            cla.pack()
            cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)
            
            clr=Button(te,text='Отмена',font='Arial 24',bg=c2,command=(lambda:te.destroy()))
            clr.pack()
            clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

            dn=[e[1:-1]for e in cr.execute('SELECT * FROM WORKER')]
            
            bt=['Имя','Фамилия','Отчество','Номер телефона','Опыт работы','Тип работы','Рабочее время']

            st=ttk.Style()
            st.theme_use("clam")
            st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
            st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
            st.map("Treeview",background=[("selected",c4)])

            table=ttk.Treeview(te,show="headings",columns=tuple(e for e in'0123456'),style="mystyle.Treeview")

            for i in range(len(bt)):
                table.heading(str(i),text=bt[i])

            for e in dn:
                table.insert('',END,values=tuple(e))

            table.pack()
            table.place(relx=0,rely=0,relwidth=0.8,relheight=1)
        
        dwr=Button(tk,text='Выбрать\nработника',font='Arial 14',bg=c2,command=wre)
        dwr.pack()
        dwr.place(relx=2/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

        def cre():
            te=Tk()
            te.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

            def enter():
                ti=int(table.focus()[1:])-1
                zn=[e for e in cr.execute('SELECT * FROM CAR')]
                dcr['text']=str(zn[ti][0])
                te.destroy()

            cla=Button(te,text='Выбрать',font='Arial 24',bg=c2,command=enter)
            cla.pack()
            cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)
            
            clr=Button(te,text='Отмена',font='Arial 24',bg=c2,command=(lambda:te.destroy()))
            clr.pack()
            clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

            dn=[e[1:-1]for e in cr.execute('SELECT * FROM CAR')]
            
            bt=['Марка','Длина','Ширина','Номер','Цвет']

            st=ttk.Style()
            st.theme_use("clam")
            st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
            st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
            st.map("Treeview",background=[("selected",c4)])

            table=ttk.Treeview(te,show="headings",columns=tuple(e for e in'01234'),style="mystyle.Treeview")

            for i in range(len(bt)):
                table.heading(str(i),text=bt[i])

            for e in dn:
                table.insert('',END,values=tuple(e))

            table.pack()
            table.place(relx=0,rely=0,relwidth=0.8,relheight=1)
        
        dcr=Button(tk,text='Выбрать\nавтомобиль',font='Arial 14',bg=c2,command=cre)
        dcr.pack()
        dcr.place(relx=3/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

        dwt=Entry(tk,font='Arial 14',justify='center',bg=c2)
        dwt.pack()
        dwt.place(relx=4/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

        dcs=Entry(tk,font='Arial 14',justify='center',bg=c2)
        dcs.pack()
        dcs.place(relx=5/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

        def add():
            co=("UPDATE LIST  SET DATE_WORK='%s',ID_CLIENT=%s,ID_WORKER=%s,ID_CAR=%s,WORK_TYPE='%s',COST=%s WHERE LIST_ID="+tid)%(ddt.get(),dcl['text'],dwr['text'],dcr['text'],dwt.get(),dcs.get())
            cr.execute(co)
            cr.commit()
            zkw()
        
        Label(tk,bg=c1).place(rely=2/3,relx=0,relwidth=1,relheight=1/3)
        Button(tk,text='Изменить',font='Arial 24',bg=c1,command=add).place(relx=0.35,rely=2/3,relwidth=0.15,relheight=1/3)
        Button(tk,text='Отмена',font='Arial 24',bg=c1,command=zkw).place(relx=0.5,rely=2/3,relwidth=0.15,relheight=1/3)


    clr=Button(tk,text='Изменить',font='Arial 24',bg=c2,command=cha)
    clr.pack()
    clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

    def rem():
        ti=int(table.focus()[1:])-1
        zn=[e for e in cr.execute('SELECT * FROM LIST')]
        cr.execute('DELETE FROM LIST WHERE LIST_ID='+str(zn[ti][0]))
        cr.commit()
        zkw()
    
    cld=Button(tk,text='Удалить',font='Arial 24',bg=c2,command=rem)
    cld.pack()
    cld.place(relx=0.8,rely=2/8,relwidth=0.2,relheight=1/8)

    mnb=Button(tk,text='К главному',font='Arial 24',bg=c2,command=main)
    mnb.pack()
    mnb.place(relx=0.8,rely=7/8,relwidth=0.2,relheight=1/8)

    iz=[e[1:-1]for e in cr.execute('SELECT * FROM LIST')]
    print(iz)
    cld=[e for e in cr.execute('SELECT * FROM CLIENT')]
    crd=[e for e in cr.execute('SELECT * FROM CAR')]
    wrd=[e for e in cr.execute('SELECT * FROM WORKER')]
    dn=[[e[0]]+['\n'.join(cld[[el[0]for el in cld].index(e[1])][2:0:-1])]+['\n'.join(wrd[[el[0]for el in wrd].index(e[2])][2:0:-1])]+['\n'.join(crd[[el[0]for el in crd].index(e[3])][1::3])]+list(e[4:])for e in iz]
    
    bt=['Дата','Клиент','Работник','Автомобиль','Вид работы','Цена']

    st=ttk.Style()
    st.theme_use("clam")
    st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
    st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
    st.map("Treeview",background=[("selected",c4)])

    table=ttk.Treeview(tk,show="headings",columns=tuple(e for e in'012345'),style="mystyle.Treeview")

    for i in range(len(bt)):
        table.heading(str(i),text=bt[i])

    for e in dn:
        table.insert('',END,values=tuple(e))

    table.pack()
    table.place(relx=0,rely=0,relwidth=0.8,relheight=1)

def zka():
    global tk
    tk.destroy()
    tk=Tk()
    tk.geometry('%dx%d+%d+%d'%(wid*0.8,heg*0.3,(wid-wid*0.8)//2,(heg-heg*0.3)//2))

    bt=['Дата','Клиент','Работник','Автомобиль','Вид работы','Цена']
    
    for i in range(len(bt)):
        Label(tk,text=bt[i],font='Arial 16',bg=c1).place(relx=i/len(bt),rely=0,relheight=1/3,relwidth=1/len(bt))
    ddt=Entry(tk,font='Arial 14',justify='center',bg=c2)
    ddt.pack()
    ddt.place(relx=0,rely=1/3,relheight=1/3,relwidth=1/len(bt))

    def cle():
        te=Tk()
        te.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

        def enter():
            ti=int(table.focus()[1:])-1
            zn=[e for e in cr.execute('SELECT * FROM CLIENT')]
            dcl['text']=str(zn[ti][0])
            te.destroy()
        
        cla=Button(te,text='Выбрать',font='Arial 24',bg=c2,command=enter)
        cla.pack()
        cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)

        clr=Button(te,text='Отмена',font='Arial 24',bg=c2,command=(lambda:te.destroy()))
        clr.pack()
        clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

        dn=[e[1:-1]for e in cr.execute('SELECT * FROM CLIENT')]
        
        bt=['Имя','Фамилия','Отчество','Номер телефона']

        st=ttk.Style()
        st.theme_use("clam")
        st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
        st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
        st.map("Treeview",background=[("selected",c4)])

        table=ttk.Treeview(te,show="headings",columns=tuple(e for e in'0123'),style="mystyle.Treeview")

        for i in range(len(bt)):
            table.heading(str(i),text=bt[i])

        for e in dn:
            table.insert('',END,values=tuple(e))

        table.pack()
        table.place(relx=0,rely=0,relwidth=0.8,relheight=1)

    dcl=Button(tk,text='Выбрать\nклиента',font='Arial 14',bg=c2,command=cle)
    dcl.pack()
    dcl.place(relx=1/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

    def wre():
        te=Tk()
        te.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

        def enter():
            ti=int(table.focus()[1:])-1
            zn=[e for e in cr.execute('SELECT * FROM WORKER')]
            dwr['text']=str(zn[ti][0])
            te.destroy()

        cla=Button(te,text='Выбрать',font='Arial 24',bg=c2,command=enter)
        cla.pack()
        cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)
        
        clr=Button(te,text='Отмена',font='Arial 24',bg=c2,command=(lambda:te.destroy()))
        clr.pack()
        clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

        dn=[e[1:-1]for e in cr.execute('SELECT * FROM WORKER')]
        
        bt=['Имя','Фамилия','Отчество','Номер телефона','Опыт работы','Тип работы','Рабочее время']

        st=ttk.Style()
        st.theme_use("clam")
        st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
        st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
        st.map("Treeview",background=[("selected",c4)])

        table=ttk.Treeview(te,show="headings",columns=tuple(e for e in'0123456'),style="mystyle.Treeview")

        for i in range(len(bt)):
            table.heading(str(i),text=bt[i])

        for e in dn:
            table.insert('',END,values=tuple(e))

        table.pack()
        table.place(relx=0,rely=0,relwidth=0.8,relheight=1)
    
    dwr=Button(tk,text='Выбрать\nработника',font='Arial 14',bg=c2,command=wre)
    dwr.pack()
    dwr.place(relx=2/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

    def cre():
        te=Tk()
        te.geometry('%dx%d+%d+%d'%(wid,heg,0,0))

        def enter():
            ti=int(table.focus()[1:])-1
            zn=[e for e in cr.execute('SELECT * FROM CAR')]
            dcr['text']=str(zn[ti][0])
            te.destroy()

        cla=Button(te,text='Выбрать',font='Arial 24',bg=c2,command=enter)
        cla.pack()
        cla.place(relx=0.8,rely=0,relwidth=0.2,relheight=1/8)
        
        clr=Button(te,text='Отмена',font='Arial 24',bg=c2,command=(lambda:te.destroy()))
        clr.pack()
        clr.place(relx=0.8,rely=1/8,relwidth=0.2,relheight=1/8)

        dn=[e[1:-1]for e in cr.execute('SELECT * FROM CAR')]
        
        bt=['Марка','Длина','Ширина','Номер','Цвет']

        st=ttk.Style()
        st.theme_use("clam")
        st.configure("Treeview",font=('Arial',14),background=c3,rowheight=int(0.9*heg/len(dn)),rowwidth=0.8*wid//len(dn[0]))
        st.configure("mystyle.Treeview.Heading", font=('Arial', 16),height=heg/10)
        st.map("Treeview",background=[("selected",c4)])

        table=ttk.Treeview(te,show="headings",columns=tuple(e for e in'01234'),style="mystyle.Treeview")

        for i in range(len(bt)):
            table.heading(str(i),text=bt[i])

        for e in dn:
            table.insert('',END,values=tuple(e))

        table.pack()
        table.place(relx=0,rely=0,relwidth=0.8,relheight=1)
    
    dcr=Button(tk,text='Выбрать\nавтомобиль',font='Arial 14',bg=c2,command=cre)
    dcr.pack()
    dcr.place(relx=3/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

    dwt=Entry(tk,font='Arial 14',justify='center',bg=c2)
    dwt.pack()
    dwt.place(relx=4/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

    dcs=Entry(tk,font='Arial 14',justify='center',bg=c2)
    dcs.pack()
    dcs.place(relx=5/len(bt),rely=1/3,relheight=1/3,relwidth=1/len(bt))

    def add():
        co="INSERT INTO LIST (DATE_WORK,ID_CLIENT,ID_WORKER,ID_CAR,WORK_TYPE,COST) VALUES ('%s',%s,%s,%s,'%s',%s)"%(ddt.get(),dcl['text'],dwr['text'],dcr['text'],dwt.get(),dcs.get())
        cr.execute(co)
        cr.commit()
        zkw()
    
    Label(tk,bg=c1).place(rely=2/3,relx=0,relwidth=1,relheight=1/3)
    Button(tk,text='Добавить',font='Arial 24',bg=c1,command=add).place(relx=0.35,rely=2/3,relwidth=0.15,relheight=1/3)
    Button(tk,text='Отмена',font='Arial 24',bg=c1,command=zkw).place(relx=0.5,rely=2/3,relwidth=0.15,relheight=1/3)

main()

author()
