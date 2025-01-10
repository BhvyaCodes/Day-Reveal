print (" Plese Enter Date betwwen 01/01/0001 and 31/12/9999")
y= int(input("Enter the year:"))
m= int(input("Enter the month:"))
d= int(input("Enter the date:"))
leap=0
if (0 < y and y < 10000 and 0 < m and m < 13) and (0 < d and d < 32) and (m==4,6,9,11) and (0 < d < 31):                                                                                                                  
      print ("You entered the date:",d,"/",m,"/",y)
      noy= (y-1)
      for i in range(1,y):
         if (i%4==0):
             leap=leap+1
      if (y%4==0) and m>2: leap=leap+1
      nom= m-1
      nod=d
      if nom== 0: nod=nod
      if nom== 1: nod=nod+31
      if nom== 2: nod=nod+59
      if nom== 3: nod=nod+90
      if nom== 4: nod=nod+120
      if nom== 5: nod=nod+151
      if nom== 6: nod=nod+181
      if nom== 7: nod=nod+212
      if nom== 8: nod=nod+243
      if nom== 9: nod=nod+273
      if nom== 10: nod=nod+304
      if nom== 11: nod=nod+334
      nod=(365*noy)+nod+leap
      print ("Total days since begining of time= ",nod)
      z=nod%7
      if z==0:print("Day is Saturday")
      elif z==1:print("Day is Sunday")
      elif z==2:print("Day is Monday")
      elif z==3:print("Day is Tueday")
      elif z==4:print("Day is Wednesday")
      elif z==5:print("Day is Thursday")
      elif z==6:print("Day is Friday")
      
else:
      print("Invalid date format")
      print (" Plese Enter Date betwwen 01/01/0001 and 31/12/9999")

   
