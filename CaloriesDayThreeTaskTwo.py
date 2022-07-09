#program to calculate calories

fat_grams = int(input("enter the number of fat grams consumed today: "))
carb_grams = int(input("enter the number of carbohydrate grams consumed today: "))
calories_fat = fat_grams * 9
print("calories fat: ",calories_fat)
calories_carb = carb_grams * 4
print("calories carbohydrate: ", calories_carb)
total_calories = calories_fat + calories_carb

print("Total calories = ",total_calories)