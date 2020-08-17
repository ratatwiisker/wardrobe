from tkinter import *
import sqlite3

#Main Window
root = Tk()
root.title('_Welcome To The Wardrobe')
#root.geometry("400x400")

#Database
conn = sqlite3.connect('allclothes.db')
c = conn.cursor()

#Login def
def login():
    global success
    credential = {"rata" : "twiisker", "buck" : "alpha"}
    success = False
    for i in range(3):
        username = u_name.get()
        password = psswd.get()
        if (credential.get(username) == password):
            success = True
            break
        else:
            u_name.delete(0, END)
            psswd.delete(0, END)
    if not success:
        window1 = Tk()
        window1.title('...')
        failed = Label(window1, text=u_name.get() + " " + "read README.txt first")
        failed.pack()

#Enter def
def enter():
    #Clear Text Boxes
    #u_name.delete(0, END)
    login()
    if success is True:
        
        root.quit()
        
        #New Window
        window = Tk()
        window.title('Wardrobe')
        greeting2 = Label(window, text="Hello" + " " + u_name.get() + "!")
        greeting2.grid(row=0, column=0, columnspan=5)
        
        
        #Buttons(Window) def

        def getall():
            window3 = Tk()
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM pullovers")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window3, text="-----Pullovers-----")
            tabel_label.grid(row=7, column=0)
            query_label = Label(window3, text=print_items)
            query_label.grid(row=8, column=0, columnspan=5)
            
            
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM socks")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window3, text="-----Socks------")
            tabel_label.grid(row=9, column=0)
            query_label = Label(window3, text=print_items)
            query_label.grid(row=10, column=0, columnspan=5)
            
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM shirts")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window3, text="-----Shirts-----")
            tabel_label.grid(row=11, column=0)
            query_label = Label(window3, text=print_items)
            query_label.grid(row=12, column=0, columnspan=5)
            
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM shorts")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window3, text="-----Shorts-----")
            tabel_label.grid(row=13, column=0)
            query_label = Label(window3, text=print_items)
            query_label.grid(row=14, column=0, columnspan=5)
            
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM boxers")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window3, text="-----Boxers-----")
            tabel_label.grid(row=15, column=0)
            query_label = Label(window3, text=print_items)
            query_label.grid(row=16, column=0, columnspan=5)
            
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM trousers")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window3, text="-----Trousers-----")
            tabel_label.grid(row=17, column=0)
            query_label = Label(window3, text=print_items)
            query_label.grid(row=18, column=0, columnspan=5)
            
            
            
            
            
        def show1():
            window2 = Tk()
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM socks")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window2, text="-----Socks------")
            tabel_label.grid(row=2, column=3)
            query_label = Label(window2, text=print_items)
            query_label.grid(row=3, column=3)
            
        def show2():
            window2 = Tk()
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM shirts")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window2, text="-----Shirts-----")
            tabel_label.grid(row=2, column=3)
            query_label = Label(window2, text=print_items)
            query_label.grid(row=3, column=3)
            
        def show3():
            window2 = Tk()
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM pullovers")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window2, text="-----Pullovers-----")
            tabel_label.grid(row=2, column=3)
            query_label = Label(window2, text=print_items)
            query_label.grid(row=3, column=3)
            
        def show4():
            window2 = Tk()
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM shorts")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window2, text="-----Shorts-----")
            tabel_label.grid(row=2, column=3)
            query_label = Label(window2, text=print_items)
            query_label.grid(row=3, column=3)
            
        def show5():
            window2 = Tk()
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM trousers")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window2, text="-----Trousers-----")
            tabel_label.grid(row=2, column=3)
            query_label = Label(window2, text=print_items)
            query_label.grid(row=3, column=3)
            
        def show6():
            window2 = Tk()
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM boxers")
            items = c.fetchall()
            print_items = ''
            for item in items:
                print_items += str(item) + "\n"
            tabel_label = Label(window2, text="-----Boxers-----")
            tabel_label.grid(row=2, column=3)
            query_label = Label(window2, text=print_items)
            query_label.grid(row=3, column=3)
        
        def getone():
            socks = Button(window, text="Socks", command=show1)
            shirts = Button(window, text="Shirts", command=show2)
            pullovers = Button(window, text="Pullovers", command=show3)
            shorts = Button(window, text="Shorts", command=show4)
            trousers = Button(window, text="Trousers", command=show5)
            boxers = Button(window, text="Boxers", command=show6)


            socks.grid(row=2, column=1)
            shirts.grid(row=3, column=1)
            pullovers.grid(row=4, column=1)
            shorts.grid(row=5, column=1)
            trousers.grid(row=6, column=1)
            boxers.grid(row=7, column=1)
            
        
        
        def addone():            
            window4 = Tk()
            conn = sqlite3.connect('allclothes.db')
            c = conn.cursor()
            #Entrys
            what = Entry(window4, width=30)
            what.grid(row=2, column=1)
            quantity = Entry(window4, width=30)
            quantity.grid(row=3, column=1)
            color = Entry(window4, width=30)
            color.grid(row=4, column=1)
            type = Entry(window4, width=30)
            type.grid(row=5, column=1)

            
            def submit(): #only adds to socks
                if what.get() is "socks" or "Socks":
                    statement = ("INSERT INTO socks VALUES (?, ?, ?)")
                    c.execute(statement, (quantity.get(), color.get(), type.get()))
                    conn.commit()
                if what.get() == "shorts" or "Shorts":
                    statement = ("INSERT INTO shorts VALUES (?, ?, ?)")
                    c.execute(statement, (quantity.get(), color.get(), type.get()))
                    conn.commit()
                if what.get() == "shirts" or "Shirts":
                    statement = ("INSERT INTO shirts VALUES (?, ?, ?)")
                    c.execute(statement, (quantity.get(), color.get(), type.get()))
                    conn.commit()
                if what.get() == "boxers" or "Boxers":
                    statement = ("INSERT INTO boxers VALUES (?, ?, ?)")
                    c.execute(statement, (quantity.get(), color.get(), type.get()))
                    conn.commit()
                if what.get() == "trousers" or "Trousers":
                    statement = ("INSERT INTO trousers VALUES (?, ?, ?)")
                    c.execute(statement, (quantity.get(), color.get(), type.get()))
                    conn.commit()
                if what.get() == "pullovers" or "Pullovers":
                    statement = ("INSERT INTO pullovers VALUES (?, ?, ?)")
                    c.execute(statement, (quantity.get(), color.get(), type.get()))
                    conn.commit()
                else:
                    no = Label(window4, text="This table doesnt exist! Check your spelling!")
                    no.grid(row=6, column=1, columnspan=2)
                
                what.delete(0, END)
                quantity.delete(0, END)
                color.delete(0, END)
                type.delete(0, END)
            
            
            #Labels
            what_label = Label(window4, text="What do you want to add:")
            what_label.grid(row=2, column=0)
            quantity_label = Label(window4, text="Quantity:")
            quantity_label.grid(row=3, column=0)
            color_label = Label(window4, text="Color:")
            color_label.grid(row=4, column=0)
            type_label = Label(window4, text="TYPE:")
            type_label.grid(row=5, column=0)
            
            submit_btn = Button(window4, text="Submit", command=submit)
            submit_btn.grid(row=6, column=0)
            
            

#Buttons
    getall = Button(window, text="Get All", command=getall)
    getone = Button(window, text="Get One", command=getone)
    addone = Button(window, text="Add One", command=addone)
    setup = Button(window, text="Setup")#, command=setup)
    delete = Button(window, text="Delete")#, command=delete)

    getall.grid(row=1, column=0)
    getone.grid(row=1, column=1)
    addone.grid(row=1, column=2)
    setup.grid(row=1, column=3)
    delete.grid(row=1, column=4)





#Entry Textboxes
u_name = Entry(root, width=30)
u_name.grid(row=1, column=1)
psswd = Entry(root, width=30, show="*")
psswd.grid(row=2, column=1)

#Label
greeting = Label(root, text="Welcome to the Wardrobe!")
greeting.grid(row=0, column=1)
u_name_label = Label(root, text="Username:")
u_name_label.grid(row=1, column=0)
psswd_label = Label(root, text="Password:")
psswd_label.grid(row=2, column=0)


#Enter Button
enter_btn = Button(root, text="Enter", command=enter)
enter_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



root.mainloop()