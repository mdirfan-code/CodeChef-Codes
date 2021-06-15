def factorial(num):#function definition
    
    fact=1;
    i=1
    while i<=num:
        fact=fact*i
        i=i+1
    return fact
num=int(input("Enter prime no: "))
num=factorial(num)
num+=int(input("rest"))
if num > 1 :
  for n in range(2, num):
    if  (num % n) == 0 :
      print(f"{num} is not Prime Number")
      break
    else:
        print(f"{num} is Prime Number")    
else:
  print(f"{num} not Prime Number")  