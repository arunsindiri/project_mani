import sqlite3
import sys

connection = sqlite3.connect("mani.db")
cursor = connection.cursor()

def labor_insert(cursor):
    SNo = int(input("Enter SNo: "))
    Type = input("Enter Type of labor: ")
    Count = int(input("Enter number: "))
    Remarks = input("Enter Remarks: ")
    
    cursor.execute("INSERT INTO labor (SNo, Type, Count, Remarks) VALUES (?,?,?,?)", (SNo, Type, Count, Remarks))
    connection.commit()
    print("Labor details inserted sucessfully")

def machinery_insert(cursor):
    SNo = int(input("Enter SNo: "))
    Discription = input("Enter Discription: ")
    Number = int(input("Enter number: "))
    Working = int(input("Enter how many machinery working: "))
    Out_of_order = int(input("Enter how many out_of_order: "))
    Remarks = input("Enter Remarks: ")

    cursor.execute("INSERT INTO machinery (SNo, Discription, Number, Working, Out_of_order, Remarks) VALUES (?,?,?,?,?,?)", (SNo, Discription, Number, Working, Out_of_order, Remarks))
    connection.commit()
    print("Machinery details inserted sucessfully")

def material_insert(cursor):
    SNo = int(input("Enter SNo: "))
    Item = input("Enter item name: ")
    Unit = input("Enter unit: ")
    Last = int(input("Enter remaining: "))
    Received = int(input("Enter Recived: "))
    Utilized = int(input("Enter Utilized: "))
    Remaining = int(input("Enter Remaining"))

    cursor.execute("INSERT INTO material (SNo, Item, Unit, Last, Received, Utilized, Remaining) VALUES(?,?,?,?,?,?,?)", (SNo, Item, Unit, Last, Received, Utilized, Remaining))
    connection.commit()
    print("Material details inserted sucessfully")

def progress_insert(cursor):
    SNo = int(input("Enter SNo: "))
    Activity = input("Enter Activity: ")
    Unit = input("Enter Units: ")
    Total_Qty = int(input("Enter Total_Qty: "))
    Executed_Qty = int(input("Enter Executed_Qty: "))
    Remarks = input("Enter Remarks: ")

    cursor.execute("INSERT INTO progress (SNo, Activity, Unit, Total_Qty, Executed_Qty, Remarks) VALUES (?,?,?,?,?,?)",(SNo, Activity, Unit, Total_Qty, Executed_Qty, Remarks))
    connection.commit()
    print("Progress details inserted sucessfully")

def money_insert(cursor):
    SNo = int(input("Enter SNo: "))
    Name_of_Vendor = input("Enter Vendor name: ")
    Type_of_work = input("Enter Type of work: ")
    Price = int(input("Enter Price: "))
    Payment = int(input("Enter Payment: "))
    Transaction_amt = int(input("Enter Transavtion amount: "))
    Balance = int(input("Enter Balance amount: "))
    bill_path = input("Enter name of bill (eg mr.bean.jpg): ")
    with open(bill_path, "rb") as f:
        bill = f.read()
        
    cursor.execute("INSERT INTO money (SNo, Name_of_Vendor, Type_of_work, Price, Payment, Transaction_amt, Balance, bill) VALUES (?,?,?,?,?,?,?,?)", (SNo, Name_of_Vendor, Type_of_work, Price, Payment, Transaction_amt, Balance, bill))  
    connection.commit()
    print("Money details inserted sucessfully")

def daily_report(cursor):
    cursor.execute("""INSERT INTO daily_report (
        Date_Time,
        Type,
        Count) SELECT datetime('now','localtime'), Type, Count FROM labour
        """)

    connection.commit()
    print("data added to daily_report sucessfully")
    
if __name__ == "__main__":
    print("Enter 1 to insert labor details: \nEnter 2 to insert machinery details: \nEnter 3 to insert material details: \nEnter 4 to insert progress details: \nEnter 5 to insert money details: \nEnter 6 to insert all tables into daily_report: ")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        labor_insert(cursor)
    elif choice == 2:
        machinery_insert(cursor)
    elif choice == 3:
        material_insert(cursor)
    elif choice == 4: 
        progress_insert(cursor)
    elif choice == 5: 
        money_insert(cursor)
    elif choice == 6: 
        daily_report(cursor)
    else:
        print("wrong choice!")
        connection.close()
