print ("Enter a date until Doomsday!")
y = int(input("Enter the year:"))
m = int(input("Enter the month:"))
d = int(input("Enter the date:"))
leap = 0
if (0<y and y<10000) and (0<m and m<13) and (0<d and d<32):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if (y%4 == 0 and y%100 != 0) or (y%400 == 0):
        month_days[1]=29
    if d > month_days[m-1]:
        print("Invalid day for",m,"/",y,"Please enter a valid day for this month.")
    else:
        print("You entered the date:",d,"/",m,"/",y)
        noy = y - 1
        for i in range(1, y):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                leap += 1
        if ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)) and m > 2:
            leap += 1            
        nom = m-1
        nod=d+ sum(month_days[:nom])
        nod=(365*noy)+nod+leap
        w = (nod)%7
        if w == 0:
            print("The day is Sunday")
        elif w == 1:
            print("The day is Monday")
        elif w == 2:
            print("The day is Tuesday")
        elif w == 3:
            print("The day is Wednesday")
        elif w == 4:
            print("The day is Thursday")
        elif w == 5:
            print("The day is Friday")
        elif w == 6:
            print("The day is Saturday")
else:
    print("Invalid date format")
    print("Please enter a date between 01/01/0001 and 31/12/9999")