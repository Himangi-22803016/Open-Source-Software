emp = {
    "ID": [],
    "Name": [],
    "Dept": [],
    "Salary": []
}

def addEmp():
    print("\nAdd New Employee")
    eId = int(input("Enter ID: "))
    name = input("Enter name: ")
    dept = input("Enter department: ")
    salary = int(input("Enter salary: "))
    emp["ID"].append(eId)
    emp["Name"].append(name)
    emp["Dept"].append(dept)
    emp["Salary"].append(salary)
    print("New Employee Added!")
    menu()

def updateRecord():
    print("\nRecord Updation")
    choice = 0
    eId = int(input("\nEnter ID of employee to update details: "))
    ind = emp["ID"].index(eId)
    print("\n1. Name\n2. Department\n3. Salary\n4. Go back")
    while choice!=4:
        choice = int(input("Enter choice: "))
        if choice == 1:
            name = input("Enter new name: ")
            emp["Name"][ind] = name
        elif choice == 2:
            dept = input("Enter new department: ")
            emp["Dept"][ind] = dept
        elif choice == 3:
            sal = int(input("Enter new salary: "))
            emp["Salary"][ind] = sal
        else:
            break
    menu()
        
def searchByID():
    print("\nSearch Employee by ID")
    eid = int(input("Enter employee ID: "))
    if eid not in emp["ID"]:
        print("ID not valid. No such employee exists.")
    else:
        ind = emp["ID"].index(eid)
        print("\nID: ", eid)
        print("Name: ", emp["Name"][ind])
        print("Department: ", emp["Dept"][ind])
        print("Salary: ", emp["Salary"][ind])
    menu()
    
def generateReport():
    dept = []
    for i in emp["Dept"]:
        if i not in dept:
            dept.append(i)
            print("Department: ", i)
            for a in emp["Dept"]:
                if a==i:
                    ind = emp["Dept"].index(a)
                    print("\nID: ", emp["ID"][ind])
                    print("Name: ", emp["Name"][ind])
                    print("Salary: ", emp["Salary"][ind])
    menu()
    
def menu():
    print("\nEmployee Directory")
    print("1. Add new Employee")
    print("2. Update existing record")
    print("3. Search employee by ID")
    print("4. Generate department-wise report")
    print("5. Exit")
    choice = int(input("\nEnter choice: "))
    if choice == 1:
        addEmp()
    elif choice == 2:
        updateRecord()
    elif choice == 3:
        searchByID()
    elif choice == 4:
        generateReport()
    else:
        print("Goodbye!")


menu()
 
