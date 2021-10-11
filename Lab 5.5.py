#Student ID: 1201201432
#student Name: Joyce Hu Xin Yi

def get_bonus(units_sold,salary):
    if(units_sold > 1000):
        bonus = salary * 0.2
    elif(units_sold >= 501 and units_sold <= 1000):
        bonus = salary * 0.1
    return bonus

def get_nett_salary(salary,bonus):
    nett = salary + bonus
    return nett

def display(id,salary,units_sold,bonus,nett_salary):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                SALARY SLIP                 ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID                : ",id)
    print("Staff salary            : RM {:.2f}".format(salary))
    print("Unit sold               : ",units_sold)
    print("Bonus                   : RM {:.2f}".format(bonus))
    print("Nett Salary             : RM {:.2f}".format(nett_salary))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                DATA ENTRY                  ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

id = int(input("Enter staff id          : "))
salary = float(input("Enter staff salary      : RM "))
units_sold = int(input("Enter total units sold  : "))

bonus = get_bonus(units_sold,salary)
nett_salary = get_nett_salary(salary,bonus)
display(id,salary,units_sold,bonus,nett_salary)

