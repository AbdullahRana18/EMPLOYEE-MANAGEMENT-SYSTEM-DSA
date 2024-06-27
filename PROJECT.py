class EmployeeNode:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.next = None

class EmployeeList:
    def __init__(self):
        self.head = None
        
    # Inserting an Employee at the end of the list
    def add_employee(self, name, employee_id, department):
        new_employee = EmployeeNode(name, employee_id, department)
        if self.head is None:
            self.head = new_employee
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_employee
        
    # Traversing the list to display all employees
    def display_all_employees(self):
        if self.head is None:
            print("\033[91mEmployee list is empty\033[0m")
            return
        print("\033[1m" + "-" * 60)
        print("|{:<20}|{:<15}|{:<20}|".format("Name", "Employee ID", "Department"))
        print("-" * 60 + "\033[0m")
        current = self.head
        while current is not None:
            print("|{:<20}|{:<15}|{:<20}|".format(current.name, current.employee_id, current.department))
            current = current.next
        print("\033[1m" + "-" * 60 + "\033[0m")

    # Searching for an employee by name using linear search
    def search_employee(self, name):
        if self.head is None:
            print("\033[91mEmployee list is empty\033[0m")
            return
        current = self.head
        while current is not None:
            if current.name == name:
                print("\033[1mEmployee found:\033[0m")
                print("\033[1m" + "-" * 60)
                print("|{:<20}|{:<15}|{:<20}|".format("Name", "Employee ID", "Department"))
                print("-" * 60 + "\033[0m")
                print("|{:<20}|{:<15}|{:<20}|".format(current.name, current.employee_id, current.department))
                print("\033[1m" + "-" * 60 + "\033[0m")
                return
            current = current.next
        print("\033[91mEmployee not found\033[0m")

    # Binary search for an employee by name
    def binary_search_employee(self, name):
        sorted_names = self.get_sorted_names()
        low = 0
        high = len(sorted_names) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_names[mid] == name:
                return self.search_employee(sorted_names[mid])
            elif sorted_names[mid] < name:
                low = mid + 1
            else:
                high = mid - 1
        print("\033[91mEmployee not found\033[0m")

    # Bubble sort for sorting employee names
    def bubble_sort(self):
        if self.head is None:
            print("\033[91mEmployee list is empty\033[0m")
            return
        swapped = True
        while swapped:
            current = self.head
            swapped = False
            while current.next is not None:
                if current.name > current.next.name:
                    current.name, current.next.name = current.next.name, current.name
                    current.employee_id, current.next.employee_id = current.next.employee_id, current.employee_id
                    current.department, current.next.department = current.next.department, current.department
                    swapped = True
                current = current.next

    # Helper function to get sorted names for binary search
    def get_sorted_names(self):
        names = []
        current = self.head
        while current is not None:
            names.append(current.name)
            current = current.next
        return sorted(names)


      

    # Inserting an Employee in sorted order based on name
    def add_employee_sorted(self, name, employee_id, department):
        new_employee = EmployeeNode(name, employee_id, department)
        if self.head is None:
            self.head = new_employee
            return
        if name < self.head.name:
            new_employee.next = self.head
            self.head = new_employee
            return
        current = self.head
        while current.next is not None and current.next.name < name:
            current = current.next
        new_employee.next = current.next
        current.next = new_employee

    # Deleting an employee by name
    def delete_employee(self, name):
        if self.head is None:
            print("\033[91mEmployee list is empty\033[0m")
            return
        if self.head.name == name:
            self.head = self.head.next
            print("\033[92mEmployee", name, "deleted successfully\033[0m")
            return
        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                print("\033[92mEmployee", name, "deleted successfully\033[0m")
                return
            current = current.next
        print("\033[91mEmployee not found\033[0m")

    # Save employee data to a text file
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            current = self.head
            while current is not None:
                file.write(f"{current.name},{current.employee_id},{current.department}\n")
                current = current.next
        print("\033[92mEmployee data saved to", filename, "successfully!\033[0m")

    # Load employee data from a text file
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(',')
                    self.add_employee(data[0], data[1], data[2])
            print("\033[92mEmployee data loaded from", filename, "successfully!\033[0m")
        except FileNotFoundError:
            print("\033[91mFile not found. Please make sure the file name is correct.\033[0m")



# Creating an instance of the EmployeeList class
employee_list = EmployeeList()

def menu():
    print("\033[1m------------------------------------Welcome to EMPLOYEE MANAGEMENT SYSTEM-------------------------------\033[0m")
    print("\n\033[1m----------------------------We Have Following Features So, Select Accordingly--------------------------\033[0m")
    print(
        "--\033[1mPress 1 For ADD EMPLOYEE (Insertion Sort)\033[0m-------- " + '\n' +
        "--\033[1mPress 2 For SEARCH EMPLOYEE (Linear Search).\033[0m----- " + '\n' +
        "--\033[1mPress 3 For SEARCH EMPLOYEE (Binary Search).\033[0m----- " + '\n' +
        "--\033[1mPress 4 For DELETE EMPLOYEE.\033[0m----- " + '\n' + 
        "--\033[1mPress 5 For DISPLAY ALL EMPLOYEES.\033[0m-- " + '\n' +
        "--\033[1mPress 6 For BUBBLE SORT.\033[0m-- " + '\n' +
        "--\033[1mPress 7 For SAVE TO FILE.\033[0m-- " + '\n' +
        "--\033[1mPress 8 For LOAD FROM FILE.\033[0m-- " + '\n' +
        "--\033[1mPress 9 For EXIT.\033[0m-- "
    )
    choice = input("\033[1mEnter your choice: \033[0m")
    if choice == '1':
        print("\033[1m------------------------------------ADD EMPLOYEE------------------------------------\033[0m")
        name = input("\033[1mEnter employee name: \033[0m")
        employee_id = input("\033[1mEnter employee ID: \033[0m")
        department = input("\033[1mEnter employee department: \033[0m")
        employee_list.add_employee_sorted(name, employee_id, department)
        print("\033[92mEmployee added successfully!\033[0m")
        print("\033[1m------------------------------------\033[0m")
        menu()
    elif choice == '2':
        print("\033[1m------------------------------------SEARCH EMPLOYEE (Linear Search)------------------------------------\033[0m")
        name = input("\033[1mEnter employee name to search: \033[0m")
        employee_list.search_employee(name)
        print("\033[1m------------------------------------\033[0m")
        menu()
    elif choice == '3':
        print("\033[1m------------------------------------SEARCH EMPLOYEE (Binary Search)------------------------------------\033[0m")
        name = input("\033[1mEnter employee name to search: \033[0m")
        employee_list.binary_search_employee(name)
        print("\033[1m------------------------------------\033[0m")
        menu()
    elif choice == '4':
        print("\033[1m------------------------------------DELETE EMPLOYEE------------------------------------\033[0m")
        name = input("\033[1mEnter employee name to delete: \033[0m")
        employee_list.delete_employee(name)
        print("\033[1m------------------------------------\033[0m")
        menu()
    elif choice == '5':
        print("\033[1m------------------------------------DISPLAY ALL EMPLOYEES------------------------------------\033[0m")
        employee_list.display_all_employees()
        print("\033[1m------------------------------------\033[0m")
        menu()
    elif choice == '6':
        print("\033[1m------------------------------------BUBBLE SORT------------------------------------\033[0m")
        employee_list.bubble_sort()
        print("\033[92mEmployee names sorted successfully!\033[0m")
        print("\033[1m------------------------------------\033[0m")
        employee_list.display_all_employees()  # Displaying all employees after sorting
        print("\033[1m------------------------------------\033[0m")
        menu()
    elif choice == '7':
        filename = input("\033[1mEnter the filename to save: \033[0m")
        employee_list.save_to_file(filename)
        menu()
    elif choice == '8':
        filename = input("\033[1mEnter the filename to load: \033[0m")
        employee_list.load_from_file(filename)
        menu()
    elif choice == '9':
        print("\033[1mEXITING...........\033[0m")
        return   
    else:
        print("\033[91mInvalid choice. Please enter a valid option.\033[0m")
        menu()


# Starting the program
menu()
