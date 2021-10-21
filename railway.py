import sqlite3
conn = sqlite3.connect("""mydatabase01.db""")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS RAILWAYS(
            tid INTEGER PRIMARY KEY,
            arr TEXT,
            dest TEXT,
            cost INTEGER
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS CLIENT(
            u_id INTEGER PRIMARY KEY,
            u_name TEXT,
            t_no INTEGER,
            cost INTEGER,
            tid INTEGER
            )""")            

def admin():    

    r = int(input("\n\tEnter number of rows to add : "))
    for i in range(0,r):
        tid = int(input("\n\tEnter train id number : "))
        arr = input("\tEnter arriving station : ")
        dest = input("\tEnter destination station : ")
        cost = int(input("\tEnter cost per seat : "))
        cur.execute("""INSERT INTO RAILWAYS VALUES(?,?,?,?)""",(tid,arr,dest,cost))

    n = 0
    while n!= 1:
        n = int(input("\n\tpress one to continue ")) 
    check_in()    

def check():

    uid = int(input(("\n\tEnter your user id : ")))
    cur.execute("""SELECT * FROM CLIENT WHERE u_id = ?""",(uid,))
    data = cur.fetchall()
    for i in data:
        name = i[1]
        id = i[0]
        no = i[2]
        cost = i[3]
        print("\n\tName of customer : ",name)
        print("\tUser id = ",id)
        print("\t total number of seats booked : ",no)
        print("total cost paid in INR : ",cost)
    n = 0
    while n!= 1:
        n = int(input("\n\tpress one to continue ")) 
    check_in()     

def info():
    
    cur.execute("""SELECT * FROM RAILWAYS""")
    data = cur.fetchall()
    print("\n\t\tShowing information about all available train(s)...")
    for i in data:
        tid = i[0]
        arr = i[1]
        dest = i[2]
        cost = i[3]
        s = "Train id = "+str(tid)+" Arriving Station = "+str(arr)+" Final Destination = "+str(dest)+" cost per seat in INR = "+str(cost)
        print(s)
    n = 0
    while n!= 1:
        n = int(input("\n\tpress one to continue "))    
    check_in()    

def receipt(uid):

    cur.execute("""SELECT * FROM CLIENT WHERE u_id = ?""",(uid,))
    data = cur.fetchall()
    i = data[0]
    name = i[1]
    no = i[2]
    cost = i[3]
    print("\f")
    print("\tName = ",name)
    print("\ttotal number of seats = ",no)
    print("\ttotal cost paid = ",cost)
    print("\tuid = ",i[0])
    n = 0
    while n!= 1:
        n = int(input("\n\tpress one to continue "))
    check_in()    

def book():
    
    cur.execute("SELECT * FROM CLIENT")
    data = cur.fetchall()
    uid = len(data)+1

    name = input("\n\tEnter your name : ")
    tid = int(input("\tEnter train id number : "))
    no = int(input("\tEnter total number of seats : "))

    cur.execute("SELECT * FROM RAILWAYS WHERE tid = ?",(tid,))
    data = cur.fetchall()
    cost = 0
    for i in data:
        cost = no*i[3]
    cur.execute("""INSERT INTO CLIENT VALUES(?,?,?,?,?)""",(uid,name,no,cost,tid))

    print("\tTicket(s) generated sucessfully generating receipt .....")

    receipt(uid)    


def cancel():

    uid = int(input("\n\tEnter your user id : "))
    cur.execute("""DELETE FROM CLIENT WHERE u_id = ?""",(uid,))
    print("\t Tickets successfully cancelled")
    n = 0
    while n!= 1:
        n = int(input("\npress one to continue "))
    check_in()    

def check_in():

    print("\n\f\t\tWelcome to XYZ Railways")
    print("\t\t-----------------------")
    print("\n\tTo check train(s) info press 1")
    print("\tTo book ticket(s) press 2")
    print("\tTo cancel ticket(s) press 3")
    print("\tTo add train details press 4")
    print("\tTo check customer details press 5")
    print("\tTo quit press 0")
    print("\n\t\tThank You")
    c = int(input("\n\n\tEnter Your choice : "))

    if c == 0 :
        return 
    elif  c==1 :
        info()
    elif c==2 :
        book()
    elif c==3 :
        cancel() 
    elif c==4:
        admin()
    elif c==5:
        check()
    else:
        print("\n\tYou have pressed a wrong option please recheck")
        check_in()
        return                 


# driver code
if __name__ == '__main__':

    check_in()