num=int(input("Enter a number:"))
def prime(num):	
  for i in range(2,num):
    if (num % i ==0):
      print("It is not a Prime number")
      break
    else:
      print("It is a Prime number")
      break 
prime(num)
