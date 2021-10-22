try:
     a=int(input("Первое число="))
     b=int(input("Второе число="))
     c=int(input("Третье число="))
except:
     print("Только число!")
     exit()
if (a%5==0) and (b%5==0) and (c%5==0):
     print() 
else:
     print("Error")
