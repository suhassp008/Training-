import database_entry as db

def insert_record():
    reg = input("Enter  USN :")
    name = input("Enter Name :")
    branch = input("Enter Branch :")
    batch = int(input("Enter Batch :"))
    marks = int(input("Enter SEM-1 Marks :"))
    db.insert_record_to_db(reg , name , branch , batch , marks)

def update_student():
    reg = input("Ente rthe USN to update the marks by 5")
    db.update_student_to_db(reg)

def remove_student():
    db.remove_student_db()    

def display_student():
    db.display_student_db()

while True:
    print("----------Student Record Management----------")
    print(" 1.Insert Student Record \n 2.Update Student Marks by 5 Mark \n 3.Remove Student Detail with Lowest Marks \n 4.Display Student Details \n 5.Exit")
    ch = int(input("Enter Your Choice :"))
    if ch == 1:
        insert_record()
    elif ch == 2:
        update_student()
    elif ch == 3:
        remove_student()
    elif ch == 4:
        display_student()
    elif ch == 5:
        exit(0)