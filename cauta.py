
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
    # function to search
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql 
        label=Label(root,text="Date Pacient",bg="red", font=('arial 14 bold'))
        label.place(x=0,y=90)
       
        sql = "SELECT * FROM PACIENT WHERE NUME LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        # creating the update form
        self.uname = Label(self.master, text="Nr fisa", font=('arial 10 bold'),bg="red")
        self.uname.place(x=0, y=140)

        self.uage = Label(self.master, text="Afectiuni", font=('arial 10 bold'),bg="red")
        self.uage.place(x=0, y=180)

        self.ugender = Label(self.master, text="Nr de telefon", font=('arial 10 bold'),bg="red")
        self.ugender.place(x=0, y=220)

        self.ulocation = Label(self.master, text="Numele tatalui", font=('arial 10 bold'),bg="red")
        self.ulocation.place(x=0, y=260)

        self.utime = Label(self.master, text="Grupa de sange ", font=('arial 10 bold'),bg="red")
        self.utime.place(x=0, y=300)

        self.uphone = Label(self.master, text="Adresa", font=('arial 10 bold'),bg="red")
        self.uphone.place(x=0, y=340)

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=260)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=300)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=340)
        self.ent6.insert(END, str(self.phone))

        # button to execute update
        self.update = Button(self.master, text="Actualizeaza", width=40, height=0, bg='green', command=self.update_db)
        self.update.place(x=600, y=660)

        # button to delete
        self.delete = Button(self.master, text="Sterge", width=40, height=0, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=660)
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.ent3.get() #updated gender
        self.var4 = self.ent4.get() #updated location
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated time
        
        query = "UPDATE PACIENT SET NUME=?, NR=?, AFECTIUNE=?, TELEFON=?, TATA=?, ADRESA=?, GRUPA=?, STARE=?, INTERNARI=?, DATA=?, ORA=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.var8, self.var9, self.var10, self.var11,self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Actualizat", "Actualizare cu scucces.")
    def delete_db(self):
        # Sterge programarea
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Sters cu succes")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
# creaza obiectul
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.mainloop()