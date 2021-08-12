from tkinter import *  

from tkinter import ttk

from tkinter import messagebox

from DataBase import Database

db = Database("Employees.db")


root = Tk()


root.title("Employee Management System")


root.geometry("1368x768+0+0")


root.state("zoom")


root.config(bg = "#2c3e50")



EmployeeName = StringVar()

age = StringVar()

DepartmentId = StringVar()

DepartmentName = StringVar()


# User input :

user_input = Frame(root , bg  = "#f5f5f5")

user_input.pack(side = TOP , fill=X)

title = Label(user_input, text="Employee Management System" , font = ("Segoe" , 18 ,"bold") , bg= "#f5f5f5" , fg = "#555" )


title.grid(row = 0 , columnspan=2 , padx = 10 , pady= 20 )


lablName = Label(user_input , text = "Employee Name" ,  font=("Segoe",15),bg="#f5f5f5" , fg="#555")

lablName.grid(row = 1 , column= 0,padx=30 , pady=30, sticky="w")

nameInput = Entry(user_input , textvariable= EmployeeName , font=("Segoe" , 16),bg="#f5f5f5" , fg="#555",width=30)

nameInput.grid(row = 1 ,column=1 , padx=30 , pady= 30, sticky="w")



lablAge = Label(user_input , text = "Employee Age" ,  font=("Segoe",15),bg="#f5f5f5" , fg="#555")

lablAge.grid(row = 1 , column= 2 ,padx=30 , pady= 30, sticky="w")

ageInput = Entry(user_input , textvariable= age , font=("Segoe" , 16),bg="#f5f5f5" , fg="#555",width=30)

ageInput.grid(row = 1 ,column= 3, padx=30 , pady= 30, sticky="w")



lablDeptId = Label(user_input , text = "DepartmentID" ,  font=("Segoe",15),bg="#f5f5f5" , fg="#555")

lablDeptId.grid(row =  2 , column= 0 ,padx=30 , pady= 30, sticky="w")

DeptIdInput = Entry(user_input , textvariable= DepartmentId, font=("Segoe" , 16),bg="#f5f5f5" , fg="#555",width=30)

DeptIdInput.grid(row = 2  ,column=  1 , padx=30 , pady= 30, sticky="w")



lablDept = Label(user_input , text = "DepartMent Name" ,  font=("Segoe",15),bg="#f5f5f5" , fg="#555")

lablDept.grid(row = 2 , column= 2 ,padx=30 , pady= 30, sticky="w")

DeptInput = Entry(user_input , textvariable= DepartmentName , font=("Segoe" , 16),bg="#f5f5f5" , fg="#555",width=30)

DeptInput.grid(row = 2 ,column= 3 , padx=30 , pady= 30, sticky="w")


def getData(e):
    selectedRow = tableView.focus()
    data  = tableView.item(selectedRow)
    global row
    row = data["values"]
    EmployeeName.set(row[1])
    age.set(row[2])
    DepartmentId.set(row[3])
    DepartmentName.set(row[4])

try:
  def displayEntries():
    #   To avoid repeatetion of records
     tableView.delete(*tableView.get_children())
     for row in db.fetch():
   
          tableView.insert("", END,values=row)
except TclError : pass

def addEntry():
   if nameInput.get() == "" or ageInput.get() == "" or DeptIdInput.get() == "" or DeptInput.get() == "":
          messagebox.showerror("Input Error!"," Kindly fill all the fields")
   else:
        db.insert(EmployeeName.get(), age.get(), DepartmentId.get(), DepartmentName.get())
        messagebox.showinfo("Success!"," Fields added successfully!")
   clearAllEntry()
   displayEntries()

def deleteEntry():
    db.remove(row[0])
    clearAllEntry()
    displayEntries()
    messagebox.showinfo("Success!","Entry Deleted SuccessFully")


def updateEntry():
    if nameInput.get() == "" or ageInput.get() == "" or DeptIdInput.get() == "" or DeptInput.get() == "":
          messagebox.showerror("Input Error!"," Select any field to update")
    else:
        db.update(row[0],EmployeeName.get(), age.get(), DepartmentId.get(), DepartmentName.get())
        messagebox.showinfo("Success!"," Fields added successfully!")
    clearAllEntry()
    displayEntries()



def clearAllEntry():
    EmployeeName.set("")
    age.set("")
    DepartmentId.set("")
    DepartmentName.set("")


buttonFrame = Frame(user_input , bg= "#f5f5f5");

buttonFrame .grid(row = 5 , columnspan=4 , padx=20 , pady= 20, sticky="w")


addButton = Button(buttonFrame ,  command = addEntry , text="Add Entry"  ,width=15 , font=("Segoe", 15 , "bold") , bg ="green" , fg="#fff").grid(row = 1 ,  column= 1, padx=30 )


updateButton = Button(buttonFrame ,  command = updateEntry , text="Update Entry"  ,width=15 , font=("Segoe", 15 , "bold") , bg ="#555" , fg="#fff").grid(row = 1 ,  column= 2, padx=30 )


deleteButton = Button(buttonFrame ,  command = deleteEntry , text="Delete Entry"  ,width=15 , font=("Segoe", 15 , "bold") , bg ="red" , fg="#fff").grid(row = 1 ,  column= 3 , padx=30 )


clearButton = Button(buttonFrame ,  command = clearAllEntry, text="Clear Entry"  ,width=15 , font=("Segoe", 15 , "bold") , bg ="blue" , fg="#fff").grid(row = 1 ,  column= 4 ,padx=30 )


#table frame :

table = Frame(root , bg= "#f2f2f2")

table.place(x = 0 , y = 338 , width = 1368 , height =700)


style = ttk.Style()


style.configure("style.Treeview" ,  font = ("Segoe" ,16) , rowheight = 30)


style.configure("style.Treeview.Heading" ,  font = ("Segoe" ,14) , rowheight = 30)

tableView = ttk.Treeview(table , columns = (1,2,3,4,5),style="style.Treeview")


tableView.heading("1" , text = "EmployeeID")
tableView.column("1" , width= 5)

tableView.heading("2" , text = "EmployeeName")
tableView.column("2" , width= 5)

tableView.heading("3", text = "Age")
tableView.column("3" , width= 5)

tableView.heading("4" , text = "DepartmentId")
tableView.column("4" , width= 5)

tableView.heading("5" , text ="DepartmentName")
tableView.column("5" , width= 5)


tableView['show'] = 'headings'
tableView.bind("<ButtonRelease-1>" , getData)
tableView.pack(fill=X)


displayEntries()



root.mainloop()