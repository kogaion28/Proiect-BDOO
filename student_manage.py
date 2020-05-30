from tkinter import *
import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("pacient.db")
    except:
        print("nu se conecteaza la baza de date")
    return conn    


def verifier():
    a=b=c=d=e=f=0
    if not student_name.get():
        t1.insert(END,"<>Numele pacientului<>\n")
        a=1
    if not roll_no.get():
        t1.insert(END,"<>Nr fisei pacientului<>\n")
        b=1
    if not branch.get():
        t1.insert(END,"<>Afectiuni<>\n")
        c=1
    if not phone.get():
        t1.insert(END,"<>Nr de Telefon<>\n")
        d=1
    if not father.get():
        t1.insert(END,"<>Numele tatalui<>\n")
        e=1
    if not address.get():
        t1.insert(END,"<>Adresa<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0


def add_student():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,ROLL_NO INTEGER,BRANCH TEXT,PHONE_NO INTEGER,FATHER TEXT,ADDRESS TEXT)")
                cur.execute("insert into PACIENT values(?,?,?,?,?,?)",(student_name.get(),int(roll_no.get()),branch.get(),int(phone.get()),father.get(),address.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"ADAUGARE CU SUCCES!!!\n")


def view_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from PACIENT")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM PACIENT WHERE ROLL_NO=?",(int(roll_no.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"PACIENT STERS CU SUCCES!!!\n")

def update_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE PACIENT SET NAME=?,ROLL_NO=?,BRANCH=?,PHONE_NO=?,FATHER=?,ADDRESS=? where ROLL_NO=?",(student_name.get(),int(roll_no.get()),branch.get(),int(phone.get()),father.get(),address.get(),int(roll_no.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"Actualizare cu succes!!!\n")


def clse():
    sys.exit() 


if __name__=="__main__":
    root=Tk()
    root.title("Gestiunea pacientilor")
     
    student_name=StringVar()
    roll_no=StringVar()
    branch=StringVar()
    phone=StringVar()
    father=StringVar()
    address=StringVar()
    
    label1=Label(root,text="Numele Pacientului:",bg="red")
    label1.place(x=0,y=0)

    label2=Label(root,text="Nr fisierului:",bg="red")
    label2.place(x=0,y=30)

    label3=Label(root,text="Afectiuni",bg="red")
    label3.place(x=0,y=60)

    label4=Label(root,text="Nr de telefon:",bg="red")
    label4.place(x=0,y=90)

    label5=Label(root,text="Numele Tatalui:",bg="red")
    label5.place(x=0,y=120)

    label6=Label(root,text="Adresa:",bg="red")
    label6.place(x=0,y=150)

    e1=Entry(root,textvariable=student_name , bg="LightGreen")
    e1.place(x=150,y=0)

    e2=Entry(root,textvariable=roll_no,bg="LightGreen")
    e2.place(x=150,y=30)

    e3=Entry(root,textvariable=branch,bg="LightGreen")
    e3.place(x=150,y=60)

    e4=Entry(root,textvariable=phone,bg="LightGreen")
    e4.place(x=150,y=90)
    
    e5=Entry(root,textvariable=father,bg="LightGreen")
    e5.place(x=150,y=120)

    e6=Entry(root,textvariable=address,bg="LightGreen")
    e6.place(x=150,y=150)
    
    t1=Text(root,width=90,height=30,bg="LightBlue")
    t1.grid(row=10,column=1)
   


    b1=Button(root,text="ADAUGA PACIENT",command=add_student,width=40,bg="blue")
    b1.grid(row=11,column=0)

    b2=Button(root,text="VEZI TOTI PACIENTI",command=view_student,width=40,bg="green")
    b2.grid(row=12,column=0)

    b3=Button(root,text="STERGE PACIENT",command=delete_student,width=40,bg="red")
    b3.grid(row=13,column=0)

    b4=Button(root,text="ACTUALIZEAZA PACIENT",command=update_student,width=40,bg="orange")
    b4.grid(row=14,column=0)

    b5=Button(root,text="INCHIDE",command=clse,width=40,bg="red")
    b5.grid(row=15,column=0)


    root.mainloop()
