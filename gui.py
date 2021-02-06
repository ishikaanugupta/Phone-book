from tkinter import *
import sqlite3

window=Tk()
window.title("Address Book")
window.geometry('300x350')


def submit():
    conn=sqlite3.connect('phone_book.db')
    c=conn.cursor()
    c.execute("INSERT INTO phone VALUES(:txt1,:txt2,:txt3,:txt4)",
              {
                  'txt1':txt1.get(),
                  'txt2':txt2.get(),
                  'txt3':txt3.get(),
                  'txt4':txt4.get()
              })
    conn.commit()
    conn.close()
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)

def query():
    conn=sqlite3.connect('phone_book.db')
    c=conn.cursor()
    c.execute("SELECT *,oid from phone")
    records=c.fetchall()

    print_records=' '
    for record in records:
        print_records+=str(record[0])+" "+"\t"+str(record[4])+"\n"

    show=Label(window,text=print_records)
    show.grid(row=9,column=1,pady=10)
    conn.commit()
    conn.close()
    
def delete():
    conn=sqlite3.connect('phone_book.db')
    c=conn.cursor()
    c.execute("DELETE from phone WHERE oid=" + txt5.get())
    txt5.delete(0,END)
    conn.commit()
    conn.close()
    


lb1=Label(window,text="Name",font=("Arial Bold",10))
lb1.grid(column=0,row=0)
txt1=Entry(window,width=20)
txt1.grid(column=1,row=0)
lb2=Label(window,text="Address",font=("Arial Bold",10))
lb2.grid(column=0,row=1)
txt2=Entry(window,width=20)
txt2.grid(column=1,row=1)
lb3=Label(window,text="Phone",font=("Arial Bold",10))
lb3.grid(column=0,row=2)
txt3=Entry(window,width=20)
txt3.grid(column=1,row=2)
lb4=Label(window,text="Email",font=("Arial Bold",10))
lb4.grid(column=0,row=3)
txt4=Entry(window,width=20)
txt4.grid(column=1,row=3)
btn4=Button(window,text="Submit",width=15,command=submit,font=("Arial Bold",10))
btn4.grid(column=1,row=4,padx=5,pady=10)
lb5=Label(window,text="Delete ID",font=("Arial Bold",10))
lb5.grid(column=0,row=5)
txt5=Entry(window,width=20)
txt5.grid(column=1,row=5)
btn2=Button(window,text="Delete",width=8,command=delete,font=("Arial Bold",10))
btn2.grid(column=1,row=6,padx=5,pady=10)
btn5=Button(window,text="Show Records",command=query,font=("Arial Bold",10))
btn5.grid(column=1,row=7,pady=10)



window.mainloop()


