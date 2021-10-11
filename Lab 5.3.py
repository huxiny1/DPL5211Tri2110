#Student ID: 1201201432
#student Name: Joyce Hu Xin Yi

def get_cm():
    cm = float(input("\nEnter centimeter : "))
    m = cm_to_meter(cm)
    print("\n{:.2f} centimeters equals to {:.2f} meters".format(cm,m))

def cm_to_meter(cm):
    meter = cm / 100
    return meter

def get_meter():
    m = float(input("\nEnter meter : "))
    cm = meter_to_cm(m)
    print("\n{:.2f} meters equals to {:.2f} centimeters".format(m,cm))

def meter_to_cm(m):
    centimeter = m * 100
    return centimeter
    
print("======================================")
print("                MENU                  ")
print("======================================")
print("  1.    Convert centimeter to meter")
print("  2.    Convert meter to centimeter")
print("======================================")
choice = int(input("Enter your choice : "))

if(choice == 1):
  get_cm()
elif(choice == 2):
  get_meter()
else:
    print("Invalid choice")

    







