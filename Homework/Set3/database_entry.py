from beautifultable import BeautifulTable
import dbcontext as db

def insert_record_to_db(reg , name , branch , batch , marks):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into student(reg_no,name,branch,batch,marks) values(?,?,?,?,?)",(reg , name , branch , batch , marks))
            print(f"Student Record  added successfully with Registration Number:{reg}")
    except Exception as e:
        print(str(e))

def update_student_to_db(reg):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select * from student where reg_no = ?",(reg ,))
            records = cursor.fetchall()
            for row in records:
                marks = row[4]
            cursor.execute("update student set marks = ? where reg_no = ?",((marks + 5),reg,))
            print("Status updated Successfully........")
    except Exception as e:
        print(f"{str(e)}")

def remove_student_db():
    
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM student WHERE marks = (SELECT min(marks) FROM student)")
            print("Record Deleted Successfully........")
    except Exception as e:
        print(f"{str(e)}")

def display_student_db():
    table = BeautifulTable()
    table.column_headers = ["USN", "Name", "Branch", "Batch", "Marks"]
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select * from student")
            records = cursor.fetchall()
            for row in records:
                table.append_row([row[0],row[1],row[2],row[3],row[4]])
            print(table)
    except Exception as e:
        print(f"{str(e)}")