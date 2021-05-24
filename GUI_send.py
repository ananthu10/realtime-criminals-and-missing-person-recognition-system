from tkinter.ttk import *
from tkinter import *

from tkinter import messagebox

import sqlite3
db = sqlite3.connect('ip.db')
# webcamIP, send_url, location,latitude, longitude
print(db)

try:
    # db = sqlite3.connect('ip.db')
    mycursor = db.cursor()
    print(mycursor)
    mycursor.execute("CREATE TABLE IP_TABLE (webcamIP TEXT (20) NOT NULL,send_url TEXT (20) NOT NULL,location TEXT (20) NOT NULL,latitude TEXT (20) NOT NULL,longitude TEXT (20) NOT NULL);")
    # mycursor.execute('''CREATE TABLE IP_TABLE (
    # ID INTEGER PRIMARY KEY AUTOINCREMENT,
    # webcamIP TEXT (20),
    # send_url TEXT (20) ,
    # location TEXT (20),
    # latitude TEXT (20),
    # longitude TEXT (20),
    # );''')

    print('table created successfully')
except sqlite3.OperationalError as msg:
    print(msg)
    print('error in operation')
    # db.rollback()
    # db.close()
# mycursor = db.cursor()
# mycursor.execute("CREATE TABLE IP_TABLE (webcamIP TEXT (20) NOT NULL,send_url TEXT (20) NOT NULL,location TEXT (20) NOT NULL,latitude TEXT (20) NOT NULL,longitude TEXT (20) NOT NULL);")
# print('table created successfully')

# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="school"
# )

# try:
#     cur =db.cursor()
#     cur.execute('''CREATE TABLE cctv (
#     StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT (20) NOT NULL,
#     age INTEGER,
#     marks REAL);''')
#     print ('table created successfully')
# except:
#     print ('error in operation')
#     db.rollback()
# db.close()

# mycursor = db.cursor()
root = Tk()
root.title("CCTV ")
root.geometry("1200x700")

# photo = PhotoImage(file='image.png')
# label12 = Label(root, image=photo).grid(row=8, column=5)

label1 = Label(root, text="web_cam_IP", width=20, height=2,
               bg="pink").grid(row=0, column=0)
label2 = Label(root, text="send_url", width=20,
               height=2, bg="pink").grid(row=1, column=0)
label3 = Label(root, text="location", width=20,
               height=2, bg="pink").grid(row=2, column=0)
label4 = Label(root, text="latitude", width=20,
               height=2, bg="pink").grid(row=3, column=0)
label5 = Label(root, text="longitude", width=20, height=2,
               bg="pink").grid(row=4, column=0)

# label6 = Label(root, text="State", width=20, height=2,
#                bg="pink").grid(row=5, column=0)
# label7 = Label(root, text="Age", width=20, height=2,
#                bg="pink").grid(row=6, column=0)
label8 = Label(root, width=10, height=2).grid(row=7, column=2)
label9 = Label(root, width=10, height=2).grid(row=7, column=4)
label10 = Label(root, width=10, height=2).grid(row=7, column=6)
label11 = Label(root, width=10, height=2).grid(row=7, column=8)


e1 = Entry(root, width=30, borderwidth=8)
e1.grid(row=0, column=1)
e2 = Entry(root, width=30, borderwidth=8)
e2.grid(row=1, column=1)
e3 = Entry(root, width=30, borderwidth=8)
e3.grid(row=2, column=1)
e4 = Entry(root, width=30, borderwidth=8)
e4.grid(row=3, column=1)
e5 = Entry(root, width=30, borderwidth=8)
e5.grid(row=4, column=1)
# e6 = Entry(root, width=30, borderwidth=8)
# e6.grid(row=5, column=1)
# e7 = Entry(root, width=30, borderwidth=8)
# e7.grid(row=6, column=1)


def Register():
    webcamIP = e1.get()
    dbRollNo = ""
    Select = "select webcamIP from IP_TABLE where webcamIP='%s'" % (webcamIP)
    mycursor.execute(Select)
    result = mycursor.fetchall()
    for i in result:
        dbipNo = i[0]
    if(webcamIP == dbRollNo):
        messagebox.askokcancel("Information", "Record Already exists")
    else:
        Insert = "Insert into IP_TABLE(webcamIP,send_url,location,latitude,longitude) values(?,?,?,?,?)"
        send_url = e2.get()
        location = e3.get()
        latitude = e4.get()
        longitude = e5.get()

        if(webcamIP != "" and send_url != "" and location != "" and latitude != "" and longitude != ""):
            Value = (webcamIP, send_url, location, latitude, longitude)
            mycursor.execute(Insert, Value)
            db.commit()
            messagebox.askokcancel("Information", "Record inserted")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
        else:
            if (webcamIP == "" and send_url == "" and location == "" and latitude == "" and longitude == ""):
                messagebox.askokcancel(
                    "Information", "New Entery Fill All Details")
            else:
                messagebox.askokcancel("Information", "Some fields left blank")

# webcamIP, send_url, location,
#                      latitude, longitude


def ShowRecord():
    webcamIP = e1.get()
    dbRollNo = ""
    Select = "select webcamIP from IP_TABLE where webcamIP='%s'" % (webcamIP)
    mycursor.execute(Select)
    result1 = mycursor.fetchall()
    for i in result1:
        dbRollNo = i[0]
    Select1 = "select send_url,location,latitude,longitude from IP_TABLE where webcamIP='%s'" % (
        webcamIP)
    mycursor.execute(Select1)
    result2 = mycursor.fetchall()
    send_url = ""
    location = ""
    latitude = ""
    longitude = ""

    if(webcamIP == dbRollNo):
        for i in result2:
            send_url = i[0]
            location = i[1]
            longitude = i[2]
            longitude = i[3]

        e2.insert(0, send_url)
        e3.insert(0, location)
        e4.insert(0, longitude)
        e5.insert(0, longitude)

    else:
        messagebox.askokcancel("Information", "No Record exists")
# webcamIP, send_url, location,latitude, longitude


def Delete():
    webcamIP = e1.get()
    Delete = "delete from IP_TABLE where webcamIP='%s'" % (webcamIP)
    mycursor.execute(Delete)
    db.commit()
    messagebox.showinfo("Information", "Record Deleted")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

# webcamIP, send_url, location,latitude, longitude


def Update():
    webcamIP = e1.get()
    send_url = e2.get()
    location = e3.get()
    latitude = e4.get()
    longitude = e5.get()
    Update = "Update IP_TABLE set send_url=?, location=?, latitude=?, longitude=? where webcamIP=? "
    Values = (send_url, location, latitude, longitude, webcamIP)
    # Update = "Update IP_TABLE set send_url=?, location=?, latitude=', longitude=?, where webcamIP=? " % (send_url, location, latitude, longitude, webcamIP)
    mycursor.execute(Update, Values)
    db.commit()
    messagebox.showinfo("Info", "Record Update")


def Showall():
    class A(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)
         # webcamIP, send_url, location,latitude, longitude

        def CreateUI(self):
            tv = Treeview(self)
            tv['columns'] = ('webcamIP', 'send_url',
                             'location', 'latitude', 'longitude')
            tv.heading('#0', text='webcamIP', anchor='center')
            tv.column('#0', anchor='center')
            tv.heading('#1', text='send_url', anchor='center')
            tv.column('#1', anchor='center')
            tv.heading('#2', text='location', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='latitude', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='longitude', anchor='center')
            tv.column('#4', anchor='center')

            tv.grid(sticky=(N, S, W, E))
            self.treeview = tv
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
        # webcamIP, send_url, location,latitude, longitude

        def LoadTable(self):
            Select = "Select * from IP_TABLE"
            mycursor.execute(Select)
            result = mycursor.fetchall()
            webcamIP = ""
            send_url = ""
            location = ""
            latitude = ""
            longitude = ""

            for i in result:
                webcamIP = i[0]
                send_url = i[1]
                location = i[2]
                latitude = i[3]
                latitude = i[4]

                self.treeview.insert("", 'end', text=webcamIP, values=(
                    send_url, location, latitude, latitude))
    root = Tk()
    root.title("Overview Page")
    A(root)


def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)


# button1 = Button(root, text="CREATE DB", width=10, height=2,
#                  command=Create_db).grid(row=7, column=0)

button1 = Button(root, text="Register", width=10, height=2,
                 command=Register).grid(row=7, column=0)
button2 = Button(root, text="Delete", width=10, height=2,
                 command=Delete).grid(row=7, column=1)
button3 = Button(root, text="Update", width=10, height=2,
                 command=Update).grid(row=7, column=3)
button4 = Button(root, text="Show record", width=10, height=2,
                 command=ShowRecord).grid(row=7, column=5)
button5 = Button(root, text="Show All", width=10, height=2,
                 command=Showall).grid(row=7, column=7)
button6 = Button(root, text="Clear", width=10, height=2,
                 command=Clear).grid(row=7, column=9)
root.mainloop()
