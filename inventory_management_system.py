from tkinter import *
from tkinter import messagebox
import os
f=open("database_proj",'a+')
root = Tk()
ijklm=-1

def additem():
    global ijklm
    num_lines = 0
    with open("database_proj", 'r') as f10:
        for line in f10:
            num_lines += 1
    ijklm=num_lines-1
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    f.write('{0} {1} {2} {3} {4}\n'.format(str(e1),e2,e3,str(e4),e5))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


def deleteitem():
    e1=entry1.get()
    with open(r"database_proj") as f, open(r"database_proj1", "w") as working:
        for line in f:
            if str(e1) not in line:
                working.write(line)
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")
    f.close()
    working.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def firstitem():
    global ijklm
    ijklm=0
    f.seek(ijklm)
    c=f.readline()
    jkl=list(c.split(" "))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry1.insert(0,str(jkl[0]))
    entry2.insert(0,str(jkl[1]))
    entry3.insert(0,str(jkl[2]))
    entry4.insert(0,str(jkl[3]))
    entry5.insert(0,str(jkl[4]))

def nextitem():
    global ijklm
    ijklm = ijklm + 1
    f.seek(ijklm)
    try:
        c=f.readlines()
        xyz = c[ijklm]
        jkl = list(xyz.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry1.insert(0, str(jkl[0]))
        entry2.insert(0, str(jkl[1]))
        entry3.insert(0, str(jkl[2]))
        entry4.insert(0, str(jkl[3]))
        entry5.insert(0, str(jkl[4]))
    except:
        messagebox.showinfo("Title", "@@@ NO MORE RECORDS @@@")
def previousitem():
        global ijklm
        ijklm=ijklm-1
        f.seek(ijklm)
        try:
            z = f.readlines()
            xyz=z[ijklm]
            jkl = list(xyz.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

            entry1.insert(0, str(jkl[0]))
            entry2.insert(0, str(jkl[1]))
            entry3.insert(0, str(jkl[2]))
            entry4.insert(0, str(jkl[3]))
            entry5.insert(0, str(jkl[4]))
        except:
            messagebox.showinfo("Title", "@@@ NO MORE RECORDS @@@")


def lastitem():
    global ijklm
    f4=open("database_proj",'r')
    x=f4.read().splitlines()
    last_line= x[-1]
    num_lines = 0
    with open("database_proj", 'r') as f8:
        for line in f8:
            num_lines += 1
    ijklm=num_lines-1
    try:
        jkl = list(last_line.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)

        entry1.insert(0, str(jkl[0]))
        entry2.insert(0, str(jkl[1]))
        entry3.insert(0, str(jkl[2]))
        entry4.insert(0, str(jkl[3]))
        entry5.insert(0, str(jkl[4]))
    except:
        messagebox.showinfo("Title", "@@@ NO MORE RECORDS @@@")


def updateitem():

    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    with open(r"database_proj") as f1, open(r"database_proj1", "w") as working:
        for line in f1:
            if str(e1) not in line:
                working.write(line)
            else:
                working.write('{0} {1} {2} {3} {4}'.format(str(e1), e2, e3, str(e4), e5))
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")


def searchitem():
    i=0
    e11 = entry1.get()
    with open(r"database_proj") as working:
        for line in working:
            i=i+1
            if str(e11) in line:
                break
        try:
            jkl = list(line.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(jkl[0]))
            entry2.insert(0, str(jkl[1]))
            entry3.insert(0, str(jkl[2]))
            entry4.insert(0, str(jkl[3]))
            entry5.insert(0, str(jkl[4]))
        except:
            messagebox.showinfo("Title", "error end of file")
    working.close()


def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


label0= Label(root,text="!!!WELCOME TO INVENTORY MANAGEMENT SYSTEM!!!", font=("Helvetica", 30))
label1=Label(root,text="ENTER ITEM NAME", font=("Helvetica", 12))
entry1=Entry(root , font=("Helvetica", 12))
label2=Label(root, text="ENTER ITEM PRICE", font=("Helvetica", 12))
entry2= Entry(root, font=("Helvetica", 12))
label3=Label(root, text="ENTER ITEM QUANTITY", font=("Helvetica", 12))
entry3= Entry(root, font=("Helvetica", 12))
label4=Label(root, text="ENTER ITEM CATEGORY", font=("Helvetica", 12))
entry4= Entry(root, font=("Helvetica", 12))
label5=Label(root, text="ENTER ITEM DISCOUNT", font=("Helvetica", 12))
entry5= Entry(root, font=("Helvetica", 12))
button1= Button(root, text="ADD ITEM", bg="black", fg="white", width=20, font=("Helvetica", 12), command=additem)
button2= Button(root, text="DELETE ITEM", bg="black", fg="white", width =20, font=("Helvetica", 12), command=deleteitem)
button3= Button(root, text="VIEW FIRST ITEM" , bg="black", fg="white", width =20, font=("Helvetica", 12), command=firstitem)
button4= Button(root, text="VIEW NEXT ITEM" , bg="black", fg="white", width =20, font=("Helvetica", 12), command=nextitem)
button5= Button(root, text="VIEW PREVIOUS ITEM", bg="black", fg="white", width =20, font=("Helvetica", 12), command=previousitem)
button6= Button(root, text="VIEW LAST ITEM", bg="black", fg="white", width =20, font=("Helvetica", 12), command=lastitem)
button7= Button(root, text="UPDATE ITEM", bg="black", fg="white", width =20, font=("Helvetica", 12), command=updateitem)
button8= Button(root, text="SEARCH ITEM", bg="black", fg="white", width =20, font=("Helvetica", 12), command=searchitem)
button9= Button(root, text="CLEAR SCREEN", bg="black", fg="white", width=20, font=("Helvetica", 12), command=clearitem)
label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=6,column=1, sticky=W, padx=10, pady=10)
label2.grid(row=7,column=1, sticky=W, padx=10, pady=10)
label3.grid(row=8,column=1, sticky=W, padx=10, pady=10)
label4.grid(row=9,column=1, sticky=W, padx=10, pady=10)
label5.grid(row=10,column=1, sticky=W, padx=10, pady=10)
entry1.grid(row=6,column=2, padx=10, pady=10)
entry2.grid(row=7,column=2, padx=10, pady=10)
entry3.grid(row=8,column=2, padx=10, pady=10)
entry4.grid(row=9,column=2, padx=10, pady=10)
entry5.grid(row=10,column=2, padx=10, pady=10)
button1.grid(row=12,column=0, padx=4, pady=10)
button2.grid(row=12,column=1, padx=4, pady=10)
button3.grid(row=12,column=2, padx=4, pady=10)
button4.grid(row=12,column=3, padx=4, pady=10)
button5.grid(row=13,column=0, padx=4, pady=10)
button6.grid(row=13,column=1, padx=4, pady=10)
button7.grid(row=13,column=2, padx=4, pady=10)
button8.grid(row=13,column=3, padx=4, pady=10)
button9.grid(row=14,column=1, padx=4, pady=10)
root.mainloop()