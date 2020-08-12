import sqlite3


#c.execute("""CREATE TABLE trousers(
 #           Quantity integer,
  #          Color text,
   #         Type text
    #        )""")
#c.execute("""CREATE TABLE shorts(
 #           Quantity integer,
  #          Color text,
   #         Type text
    #        )""")
#c.execute("""CREATE TABLE boxers(
 #           Quantity integer,
  #          Color text,
   #         Type text
    #        )""")
#c.execute("""CREATE TABLE shirts(
 #           Quantity integer,
  #          Color text,
   #         Type text
    #        )""")
#c.execute("""CREATE TABLE pullovers(
 #           Quantity integer,
  #          Color text,
   #         Type text
    #        )""")
#c.execute("""CREATE TABLE socks(
 #           Quantity integer,
  #          Color text,
   #         Type text
    #        )""")
    
    
#c.execute("INSERT INTO socks VALUES ('3', 'green', 'short')")

def getall():
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    print("Connected to SQLite3")
    
    sqlite_select_query = """SELECT * from socks"""
    c.execute(sqlite_select_query)
    print("---------socks---------")
    items = c.fetchall()
    for item in items:
        print(str(item[0]) + "\t " + item[1] + "\t" + item[2])
        print("")
    conn.commit()
    
    sqlite_select_query = """SELECT * from trousers"""
    c.execute(sqlite_select_query)
    print("-------trousers----------")
    items = c.fetchall()
    for item in items:
        print(str(item[0]) + " \t" + item[1] + "\t" + item[2])
        print("")
    conn.commit()
    
    sqlite_select_query = """SELECT * from boxers"""
    c.execute(sqlite_select_query)
    print("---------boxers--------")
    items = c.fetchall()
    for item in items:
        print(str(item[0]) + " \t" + item[1] + "\t" + item[2])
        print("")
    conn.commit()
    
    sqlite_select_query = """SELECT * from shorts"""
    c.execute(sqlite_select_query)
    print("-------shorts----------")
    items = c.fetchall()
    for item in items:
        print(str(item[0]) + "\t " + item[1] + "\t" + item[2])
        print("")
    conn.commit()
    
    sqlite_select_query = """SELECT * from pullovers"""
    c.execute(sqlite_select_query)
    print("---------pullovers----------")
    items = c.fetchall()
    for item in items:
        print(str(item[0]) + " \t" + item[1] + "\t" + item[2])
        print("")
    conn.commit()
    
    sqlite_select_query = """SELECT * from shirts"""
    c.execute(sqlite_select_query)
    print("-------shirts--------")
    items = c.fetchall()
    for item in items:
        print(str(item[0]) + " \t" + item[1] + "\t" + item[2])
    conn.commit()
    
def getone():
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    print("Connected to SQLite3")
    
    user_input0 = input("What are you looking for?\n")
    if user_input0 == "socks":
        statement0 = ("""SELECT * FROM socks """)
        c.execute(statement0)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + "\t " + item[1] + "\t" + item[2])
        conn.commit()
        conn.close()
    
    elif user_input0 == "trousers":
        statement0 = ("""SELECT * FROM trouser """)
        c.execute(statement0)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + "\t " + item[1] + "\t" + item[2])
        conn.commit()
        conn.close()
    
    elif user_input0 == "shorts":
        statement0 = ("""SELECT * FROM shorts """)
        c.execute(statement0)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + " \t" + item[1] + "\t" + item[2])
        conn.commit()
        conn.close()
    
    elif user_input0 == "boxers":
        statement0 = ("""SELECT * FROM boxers """)
        c.execute(statement0)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + " \t" + item[1] + "\t" + item[2])
        conn.commit()
        conn.close()
        
    elif user_input0 == "shirts":
        statement0 = ("""SELECT * FROM shirts """)
        c.execute(statement0)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + " \t" + item[1] + "\t" + item[2])
        conn.commit()
        conn.close()
        
    elif user_input0 == "pullovers":
        statement0 = ("""SELECT * FROM pullovers """)
        c.execute(statement0)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + " \t" + item[1] + "\t" + item[2])
        conn.commit()
        conn.close()
    
    
def addone():
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    print("Connected to SQLite3")
    
    user_input1 = input("What do you want to add?")
    user_input2 = input("How many?")
    user_input3 = input("In what color?")
    user_input4 = input("What type is it?")
    
    if user_input1 == "socks":
        statement1 = ("INSERT INTO socks VALUES (?,?,?)")
        c.execute(statement1, (user_input2, user_input3, user_input4))
        conn.commit()
        conn.close()
    elif user_input1 == "trousers":
        statement1 = ("INSERT INTO trousers VALUES (?,?,?)")
        c.execute(statement1, (user_input2, user_input3, user_input4))
        conn.commit()
        conn.close()
    elif user_input1 == "boxers":
        statement1 = ("INSERT INTO boxers VALUES (?,?,?)")
        c.execute(statement1, (user_input2, user_input3, user_input4))
        conn.commit()
        conn.close()
    elif user_input1 == "shorts":
        statement1 = ("INSERT INTO shorts VALUES (?,?,?)")
        c.execute(statement1, (user_input2, user_input3, user_input4))
        conn.commit()
        conn.close()
    elif user_input1 == "pullovers":
        statement1 = ("INSERT INTO pullovers VALUES (?,?,?)")
        c.execute(statement1, (user_input2, user_input3, user_input4))
        conn.commit()
        conn.close()
    elif user_input1 == "shirts":
        statement1 = ("INSERT INTO shirts VALUES (?,?,?)")
        c.execute(statement1, (user_input2, user_input3, user_input4))
        conn.commit()
        conn.close()


def setup():
    print("""Hello to your set up.
Here you will configure your wardrobe for the first time
""")
        
    user_input5 = input("If you want to add your wardrobe press Y if not press N")
    if user_input5 == "y" or "Y":
        while user_input5 == "y":
            user_input6 = input("What to you want to add?")
            if user_input6 == "socks":
                conn = sqlite3.connect('allclothes.db')
                c = conn.cursor()
                user_input2 = input("How many?")
                user_input3 = input("In what color?")
                user_input4 = input("What type is it?")
                statement2 = ("INSERT INTO socks VALUES (?,?,?)")
                c.execute(statement2, (user_input2, user_input3, user_input4))
                conn.commit()
                user_input5 = input("If you want to add your wardrobe press Y if not press N")

            if user_input6 == "trousers":
                conn = sqlite3.connect('allclothes.db')
                c = conn.cursor()
                user_input2 = input("How many?")
                user_input3 = input("In what color?")
                user_input4 = input("What type is it?")
                statement2 = ("INSERT INTO trousers VALUES (?,?,?)")
                c.execute(statement2, (user_input2, user_input3, user_input4))
                conn.commit()
                user_input5 = input("If you want to add your wardrobe press Y if not press N")

            if user_input6 == "boxers":
                conn = sqlite3.connect('allclothes.db')
                c = conn.cursor()
                user_input2 = input("How many?")
                user_input3 = input("In what color?")
                user_input4 = input("What type is it?")
                statement2 = ("INSERT INTO boxers VALUES (?,?,?)")
                c.execute(statement2, (user_input2, user_input3, user_input4))
                conn.commit()
                user_input5 = input("If you want to add your wardrobe press Y if not press N")
            
            if user_input6 == "shorts":
                conn = sqlite3.connect('allclothes.db')
                c = conn.cursor()
                user_input2 = input("How many?")
                user_input3 = input("In what color?")
                user_input4 = input("What type is it?")
                statement2 = ("INSERT INTO shorts VALUES (?,?,?)")
                c.execute(statement2, (user_input2, user_input3, user_input4))
                conn.commit()
                user_input5 = input("If you want to add your wardrobe press Y if not press N")


            if user_input6 == "pullovers":
                conn = sqlite3.connect('allclothes.db')
                c = conn.cursor()
                user_input2 = input("How many?")
                user_input3 = input("In what color?")
                user_input4 = input("What type is it?")
                statement2 = ("INSERT INTO pullovers VALUES (?,?,?)")
                c.execute(statement2, (user_input2, user_input3, user_input4))
                conn.commit()
                user_input5 = input("If you want to add your wardrobe press Y if not press N")


            if user_input6 == "shirts":
                conn = sqlite3.connect('allclothes.db')
                c = conn.cursor()
                user_input2 = input("How many?")
                user_input3 = input("In what color?")
                user_input4 = input("What type is it?")
                statement2 = ("INSERT INTO shirts VALUES (?,?,?)")
                c.execute(statement2, (user_input2, user_input3, user_input4))
                conn.commit()
                user_input5 = input("If you want to add your wardrobe press Y if not press N")

                
    if user_input5 == "n" or "N":
        user_input7 = input ("What else do you wanna do?\n (add one/ get one/ get all/ set up)")
        if user_input7 == "add one":
            addone()
        elif user_input7 == "get one":
            getone()
        elif user_input7 == "get all":
            getall()
        elif user_input7 == "set up":
            setup()          
        
def delete():
    user_input8 = input("What do you want to delete?")
    if user_input8 == "socks":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement3 = ("""SELECT * FROM socks """)
        c.execute(statement3)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + "\t " + item[1] + "\t" + item[2])
        user_input9 = input("What color are they?")
        user_input10 = input("What type are they?")
        statement4 = ("""DELETE from socks WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (user_input9, user_input10))
        conn.commit()
        conn.close()
        print("!DELETED!")
        
    if user_input8 == "trousers":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement3 = ("""SELECT * FROM trousers """)
        c.execute(statement3)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + "\t " + item[1] + "\t" + item[2])
        user_input9 = input("What color are they?")
        user_input10 = input("What type are they?")
        statement4 = ("""DELETE from trousers WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (user_input9, user_input10))
        conn.commit()
        conn.close()
        print("!DELETED!")
        
    if user_input8 == "boxers":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement3 = ("""SELECT * FROM boxers """)
        c.execute(statement3)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + " \t" + item[1] + "\t" + item[2])
        user_input9 = input("What color are they?")
        user_input10 = input("What type are they?")
        statement4 = ("""DELETE from boxers WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (user_input9, user_input10))
        conn.commit()
        conn.close()
        print("!DELETED!")
        
    if user_input8 == "shorts":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement3 = ("""SELECT * FROM shorts """)
        c.execute(statement3)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + "\t " + item[1] + "\t" + item[2])
        user_input9 = input("What color are they?")
        user_input10 = input("What type are they?")
        statement4 = ("""DELETE from shorts WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (user_input9, user_input10))
        conn.commit()
        conn.close()
        print("!DELETED!")
        
    if user_input8 == "pullovers":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement3 = ("""SELECT * FROM pullovers """)
        c.execute(statement3)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + "\t " + item[1] + "\t" + item[2])
        user_input9 = input("What color are they?")
        user_input10 = input("What type are they?")
        statement4 = ("""DELETE from pullovers WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (user_input9, user_input10))
        conn.commit()
        conn.close()
        print("!DELETED!")
        
    if user_input8 == "shirts":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement3 = ("""SELECT * FROM shirts """)
        c.execute(statement3)
        items = c.fetchall()
        for item in items:
            print(str(item[0]) + "\t " + item[1] + "\t" + item[2])
        user_input9 = input("What color are they?")
        user_input10 = input("What type are they?")
        statement4 = ("""DELETE from shirts WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (user_input9, user_input10))
        conn.commit()
        conn.close()
        print("!DELETED!")
        
print("Welcome to your wardrobe!\n If it is your first visit pls go to set up!")
question = input("""What do you want to do?\n
add one/ get one/ get all/ set up/ delete\n
""")
    
if question == "add one":
    addone()
elif question == "get one":
    getone()
elif question == "get all":
    getall()
elif question == "set up":
    setup()
elif question == "delete":
    delete()
