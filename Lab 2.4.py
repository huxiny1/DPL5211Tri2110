#Student ID: 1201201432
#Student Name: Joyce Hu Xin Yi

print("Invoice for Fruits Purchase")
print("---------------------------------")

comb = 1.5
kg = 5.60

qty1 = int(input("\nEnter the quantity (comb) of bananas bought: "))
qty2 = int(input("Enter the amount (kg) of grapes bought: "))

bananas = qty1 * comb
graphs = qty2 * kg
total = bananas + graphs

print("\nItem\t\tQty\tPrice\tTotal")
print("Banana (combs)\t{}\tRM{:.2f}\tRM{:.2f}".format(qty1,comb,bananas))
print("Grapes (kg)\t{}\tRM{:.2f}\tRM{:.2f}".format(qty2,kg,graphs))
print("\nTotal: RM{:.2f}".format(total))