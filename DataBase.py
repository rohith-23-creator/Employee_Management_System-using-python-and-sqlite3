import sqlite3
# from db import database
class Database:
    count  = 0
    def __init__(self,db) :
        # Connecting db
        # self.count += 1
        self.con = sqlite3.connect(db)
        # Cursor object for executing queries(insert, update ,delete)
        self.cur = self.con.cursor()
        # Queries
        sql = """
          CREATE TABLE IF NOT EXISTS EMPLOYEES(
             id Integer Primary Key,
             EmpName text,
             age integer,
             deptId Integer,
             departmentName text
          )
        """
        self.cur.execute(sql)
        # Commiting the connection
        self.con.commit()    

    #insert func (user input)
    def insert(self , EmpName, age , deptId, departmentName):        
        self.cur.execute("insert into employees values(NULL,? , ?, ? , ? )", (EmpName, age , deptId , departmentName))
        self.con.commit()   

    # printing the datas :
    def fetch(self):
        self.cur.execute("SELECT * from employees");
        rows = self.cur.fetchall();
        return rows
        # return rows
        # self.cur.close()
       
    # deleting the records :
    def remove(self ,id):
        self.cur.execute("Delete from employees where id = ? " , (id,))
        self.con.commit()

    # Update records :
    def update(self , id ,  EmpName, age , deptId, departmentName):
        self.cur.execute("update employees set EmpName = ? , age = ? , deptId = ? , departmentName = ? where id = ? ", ( EmpName, age , deptId, departmentName, id))

        self.con.commit()


obj = Database("Employees.db")
print(obj.fetch())