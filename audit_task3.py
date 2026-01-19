#using functions 
def fizzbuzz(num):
  if num%3==0 and num%5==0:
    return "FizzBuzz"
  elif num%3==0:
    return "Fizz"
  elif num%5==0:
    return "Buzz"
  else : 
    return str(num)
number=int(input("Enter a number: "))
for x in range(1,number+1):
  print(fizzbuzz(x))
