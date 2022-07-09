area = int(input("enter area to be painted: "))
price = int(input("enter price of paint per gallon: "))
number_of_gallons_required = area/115
hours_of_labour = number_of_gallons_required * 8
cost_of_the_paint = price * number_of_gallons_required
labour_charges = hours_of_labour * 20
total_cost = cost_of_the_paint + labour_charges

print("number of gallons:{:.2f} ".format(number_of_gallons_required)) 
print("hours of labour: {:.2f} ".format(hours_of_labour))
print("cost of the paint: {:.2f} ".format(cost_of_the_paint))
print("labour charges: {:.2f} ".format(labour_charges))
print("total cost = {:.2f} ".format(total_cost))