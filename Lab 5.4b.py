#Student ID: 1201201432
#student Name: Joyce Hu Xin Yi

def rectangle(w,l):
    area = w * l
    return area

def triangle(w,l):
    area = w * l / 2
    return area

i = 0
while(i<2):
    width = int(input("Enter width   : "))
    length = int(input("Enter length  : "))

    area_of_r = rectangle(width,length)
    area_of_t = triangle(width,length)

    print("\nRectangle area : {:.2f}".format(area_of_r))
    print("Triangle area  : {:.2f}\n\n".format(area_of_t))
    i += 1