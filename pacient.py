from tkinter import *
import sqlite3,sys



#conexiunea cu baza de date 
def connection():
    try:
        conn=sqlite3.connect("pacient.db")
    except:
        print("nu se conecteaza la baza de date")
    return conn    


#verificare 
def verifier():
    a=b=c=d=e=f=g=h=i=j=k=v=0
    if not pacient_nume.get():
        t1.insert(END,"<>Numele pacientului<>\n")
        a=1
    if not NR.get():
        t1.insert(END,"<>Varsta<>\n")
        b=1
    if not AFECTIUNE.get():
        t1.insert(END,"<>Afectiuni<>\n")
        c=1
    if not TELEFON.get():
        t1.insert(END,"<>NR de Telefon<>\n")
        d=1
    if not TATA.get():
        t1.insert(END,"<>Numele tatalui<>\n")
        e=1
    if not ADRESA.get():
        t1.insert(END,"<>Adresa<>\n")
        f=1
    if not GRUPA.get():
        t1.insert(END,"<>Grupa<>\n")
        g=1
    if not STARE.get():
        t1.insert(END,"<>Stare<>\n")
        h=1
    if not INTERNARI.get():
        t1.insert(END,"<>Internari<>\n")
        i=1
    if not DATA.get():
        t1.insert(END,"<>Data<>\n")
        j=1
    if not ORA.get():
        t1.insert(END,"<>Ora<>\n")
        k=1
    if not ID.get():
        t1.insert(END,"<>Nr fisier<>\n")
        v=1
    

    
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1 or k==1 or v==1:
        return 1
    else:
        return 0

#Adauga pacient
def add_pacient():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS PACIENT(NUME TEXT,NR INTEGER,AFECTIUNE TEXT,TELEFON INTEGER,TATA TEXT,ADRESA TEXT,GRUPA TEXT,STARE TEXT,INTERNARI TEXT,DATA INTEGER,ORA INTEGER,ID INTEGER)")#creaza baza de data daca nu exista
                cur.execute("insert into PACIENT values(?,?,?,?,?,?,?,?,?,?,?,?)",(pacient_nume.get(),int(NR.get()),AFECTIUNE.get(),int(TELEFON.get()),TATA.get(),ADRESA.get(),GRUPA.get(),STARE.get(),INTERNARI.get(),DATA.get(),ORA.get(),ID.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"ADAUGARE CU SUCCES!!!\n")

#Afiseaza pacienti
def view_pacient():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from PACIENT")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")

#Sterge pacient
def delete_pacient():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM PACIENT WHERE NR=?",(int(NR.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"PACIENT STERS CU SUCCES!!!\n")
#Actualizaeaza  pacient
def update_pacient():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE PACIENT SET NUME=?,NR=?,AFECTIUNE=?,TELEFON=?,TATA=?,ADRESA=?,GRUPA=?,STARE=?,INTERNARI=?,DATA=?,ORA=?,ID=? where NR=?",(pacient_nume.get(),int(NR.get()),AFECTIUNE.get(),int(TELEFON.get()),TATA.get(),ADRESA.get(),GRUPA.get(),STARE.get(),INTERNARI.get(),DATA.get(),ORA.get(),ID.get(),int(NR.get())))     #actualizeaza pacient dupa
        conn.commit()
        conn.close()
        t1.insert(END,"Actualizare cu succes!!!\n")
#------////////////////////---------------------------------












#-----/////////////////////////////-----------------------------


def clse():
    sys.exit() 


if __name__=="__main__":
    root=Tk()
    root.title("Gestiunea pacientilor")
#variabile
    pacient_nume=StringVar()
    NR=StringVar()
    AFECTIUNE=StringVar()
    TELEFON=StringVar()
    TATA=StringVar()
    ADRESA=StringVar()
    GRUPA=StringVar()
    STARE=StringVar()
    INTERNARI=StringVar()
    DATA=StringVar()
    ORA=StringVar()
    ID=StringVar()
#lebel
    label1=Label(root,text="Numele Pacientului:",bg="red")
    label1.place(x=0,y=0)

    label2=Label(root,text="Varsta Pacientului:",bg="red")
    label2.place(x=0,y=30)

    label3=Label(root,text="Afectiuni",bg="red")
    label3.place(x=0,y=60)

    label4=Label(root,text="NR de telefon:",bg="red")
    label4.place(x=0,y=90)

    label5=Label(root,text="Numele Tatalui:",bg="red")
    label5.place(x=0,y=120)

    label6=Label(root,text="Adresa:",bg="red")
    label6.place(x=0,y=150)

    label7=Label(root,text="Grupa de sange:",bg="red")
    label7.place(x=0,y=180)

    label8=Label(root,text="Stare de sanatate:",bg="red")
    label8.place(x=0,y=210)

    label9=Label(root,text="Internari la spital:",bg="red")
    label9.place(x=0,y=240)

    label10=Label(root,text="Data programari:",bg="red")
    label10.place(x=0,y=270)

    label11=Label(root,text="Ora programari:",bg="red")
    label11.place(x=0,y=300)
    
    label12=Label(root,text="Nr fisa:",bg="red")
    label12.place(x=0,y=330)



#casutele
    e1=Entry(root,textvariable=pacient_nume , bg="LightGreen")
    e1.place(x=150,y=0)

    e2=Entry(root,textvariable=NR,bg="LightGreen")
    e2.place(x=150,y=30)

    e3=Entry(root,textvariable=AFECTIUNE,bg="LightGreen")
    e3.place(x=150,y=60)

    e4=Entry(root,textvariable=TELEFON,bg="LightGreen")
    e4.place(x=150,y=90)
    
    e5=Entry(root,textvariable=TATA,bg="LightGreen")
    e5.place(x=150,y=120)

    e6=Entry(root,textvariable=ADRESA,bg="LightGreen")
    e6.place(x=150,y=150)

    e7=Entry(root,textvariable=GRUPA,bg="LightGreen")
    e7.place(x=150,y=180)

    e8=Entry(root,textvariable=STARE,bg="LightGreen")
    e8.place(x=150,y=210)

    e9=Entry(root,textvariable=INTERNARI,bg="LightGreen")
    e9.place(x=150,y=240)

    e10=Entry(root,textvariable=DATA,bg="LightGreen")
    e10.place(x=150,y=270)

    e11=Entry(root,textvariable=ORA,bg="LightGreen")
    e11.place(x=150,y=300)

    e12=Entry(root,textvariable=ID,bg="LightGreen")
    e12.place(x=150,y=330)
    
    t1=Text(root,width=90,height=30,bg="LightBlue")
    t1.grid(row=10,column=1)
    
    

#butoane
    b1=Button(root,text="ADAUGA PACIENT",command=add_pacient,width=87,bg="blue")
    b1.grid(row=12,column=1)

    b2=Button(root,text="VEZI TOTI PACIENTI",command=view_pacient,width=87,bg="green")
    b2.grid(row=13,column=1)

    b3=Button(root,text="STERGE PACIENT",command=delete_pacient,width=87,bg="red")
    b3.grid(row=14,column=1)

    b4=Button(root,text="ACTUALIZEAZA PACIENT",command=update_pacient,width=87,bg="orange")
    b4.grid(row=15,column=1)
    
    b6=Button(root,text="Cauta",command=clse,width=40,bg="red")
    b6.grid(row=13,column=0)


    b5=Button(root,text="INCHIDE PROGRAMUL",command=clse,width=40,bg="red")
    b5.grid(row=15,column=0)






    root.mainloop()
