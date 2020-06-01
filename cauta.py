
from tkinter import *
import tkinter.messagebox 
import sqlite3

conn = sqlite3.connect('pacient.db')
c = conn.cursor()


class Application:
    def __init__(self, master):
        self.master = master
        

        # cauta 
        self.name = Label(master, text="Introdu numele pacientului",bg="red")# font=('arial 18 bold'))
        self.name.place(x=0, y=5)

        # Casuta de introducere a numelui
        self.namenet = Entry(master, width=125,bg="LightGreen")
        self.namenet.place(x=190, y=4)

        # butonul de cautare 
        self.search = Button(master, text="Cauta pacientul", width=146, height=1, bg='green', command=self.search_db)
        self.search.place(x=2, y=40)
    # Functia de cautare
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql 
        label=Label(root,text="Date Pacient",bg="red", font=('arial 14 bold'))
        label.place(x=0,y=90)
       
        sql = "SELECT * FROM PACIENT WHERE NUME LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.nume = self.row[0]
            self.varsta = self.row[1]
            self.afectiune = self.row[2]
            self.telefon = self.row[3]
            self.tata = self.row[4]
            self.adresa = self.row[5]
            #---------Eroare 
            self.grupa = self.row[6]
            self.stare = self.row[7]
            self.internari = self.row[8]
            self.data = self.row[9]
            self.ora = self.row[10]
            self.id = self.row[11]
        # crearea formatului de actualizare 
        self.unume = Label(self.master, text="Nume Pacient", font=('arial 10 bold'),bg="red")
        self.unume.place(x=0, y=140)

        self.uvarsta = Label(self.master, text="Varsta", font=('arial 10 bold'),bg="red")
        self.uvarsta.place(x=0, y=180)

        self.uafectiune = Label(self.master, text="Afectiuni", font=('arial 10 bold'),bg="red")
        self.uafectiune.place(x=0, y=220)

        self.utelefon = Label(self.master, text="Numar de telefon", font=('arial 10 bold'),bg="red")
        self.utelefon.place(x=0, y=260)

        self.utata = Label(self.master, text="Tata ", font=('arial 10 bold'),bg="red")
        self.utata.place(x=0, y=300)

        self.uadresa = Label(self.master, text="Adresa", font=('arial 10 bold'),bg="red")
        self.uadresa.place(x=0, y=340)

        self.ugrupa = Label(self.master, text="Grupa", font=('arial 10 bold'),bg="red")
        self.ugrupa.place(x=0, y=370)

        self.ustare = Label(self.master, text="Stare", font=('arial 10 bold'),bg="red")
        self.ustare.place(x=0, y=400)

        self.uinternari = Label(self.master, text="Internari", font=('arial 10 bold'),bg="red")
        self.uinternari.place(x=0, y=430)

        self.udata = Label(self.master, text="Data programari", font=('arial 10 bold'),bg="red")
        self.udata.place(x=0, y=460)

        self.uora = Label(self.master, text="Ora programari", font=('arial 10 bold'),bg="red")
        self.uora.place(x=0, y=490)

        self.uid = Label(self.master, text="Nr fisier", font=('arial 10 bold'),bg="red")
        self.uid.place(x=0, y=520)

        # Casutele unde intra datele cautate
        self.ent1 = Entry(self.master, width=110, bg="LightGreen")
        self.ent1.place(x=180, y=140)
        self.ent1.insert(END, str(self.nume))

        self.ent2 = Entry(self.master, width=110, bg="LightGreen")
        self.ent2.place(x=180, y=180)
        self.ent2.insert(END, str(self.varsta))

        self.ent3 = Entry(self.master, width=110, bg="LightGreen")
        self.ent3.place(x=180, y=220)
        self.ent3.insert(END, str(self.afectiune))

        self.ent4 = Entry(self.master, width=110, bg="LightGreen")
        self.ent4.place(x=180, y=260)
        self.ent4.insert(END, str(self.telefon))

        self.ent5 = Entry(self.master, width=110, bg="LightGreen")
        self.ent5.place(x=180, y=300)
        self.ent5.insert(END, str(self.tata))

        self.ent6 = Entry(self.master, width=110, bg="LightGreen")
        self.ent6.place(x=180, y=340)
        self.ent6.insert(END, str(self.adresa))

        self.ent7 = Entry(self.master, width=110, bg="LightGreen")
        self.ent7.place(x=180, y=370)
        self.ent7.insert(END, str(self.grupa))

        self.ent8 = Entry(self.master, width=110, bg="LightGreen")
        self.ent8.place(x=180, y=400)
        self.ent8.insert(END, str(self.stare))


        self.ent9 = Entry(self.master, width=110, bg="LightGreen")
        self.ent9.place(x=180, y=430)
        self.ent9.insert(END, str(self.internari))


        self.ent10 = Entry(self.master, width=110, bg="LightGreen")
        self.ent10.place(x=180, y=460)
        self.ent10.insert(END, str(self.data))

        self.ent11 = Entry(self.master, width=110, bg="LightGreen")
        self.ent11.place(x=180, y=490)
        self.ent11.insert(END, str(self.ora))


        self.ent12 = Entry(self.master, width=110, bg="LightGreen")
        self.ent12.place(x=180, y=530)
        self.ent12.insert(END, str(self.id))

        # buton de actualizare 
        self.update = Button(self.master, text="Actualizeaza", width=40, height=0, bg='green', command=self.update_db)
        self.update.place(x=600, y=660)

        # buton de stergere 
        self.delete = Button(self.master, text="Sterge", width=40, height=0, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=660)
    def update_db(self):
        # declarea variabilelor pentru actualizare
        self.var1 = self.ent1.get() 
        self.var2 = self.ent2.get() 
        self.var3 = self.ent3.get() 
        self.var4 = self.ent4.get() 
        self.var5 = self.ent5.get() 
        self.var6 = self.ent6.get() 
        self.var7 = self.ent7.get()
        self.var8 = self.ent8.get()
        self.var9 = self.ent9.get()
        self.var10 = self.ent10.get()
        self.var11 = self.ent11.get()
        self.var12 = self.ent12.get()
        
        
        query = "UPDATE PACIENT SET NUME=?, NR=?, AFECTIUNE=?, TELEFON=?, TATA=?, ADRESA=?, GRUPA=?, STARE=?, INTERNARI=?, DATA=?, ORA=? , ID=? WHERE NUME LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.var8, self.var9, self.var10,self.var11,self.var12, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Actualizat", "Actualizare cu scucces.")
    def delete_db(self):
        # Sterge data
        sql2 = "DELETE FROM PACIENT WHERE NUME LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Sters cu succes")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
        self.ent7.destroy()
        self.ent8.destroy()
        self.ent9.destroy()
        self.ent10.destroy()
        self.ent11.destroy()
        self.ent12.destroy()
# creaza obiectul
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(True, True)
root.mainloop()