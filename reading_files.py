employee_file = open("employee.txt", "r")
for employee in employee_file.readlines():
    print(employee)
# print(employee_file.readlines()[1])
employee_file.close()