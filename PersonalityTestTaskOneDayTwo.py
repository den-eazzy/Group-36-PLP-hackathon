
books = int(input("enter number of books: "))
points = 0
if books == 0:
    print("you have ", points ,"points")
elif books == 1:
    points = 6
    print("you have ", points ,"points")
elif books == 2:
    points = 16
    print("you have ", points ,"points")
elif books == 3:
    points = 32
    print("you have ", points ,"points")
else:
    points = 60
    print("you have ", points ,"points")