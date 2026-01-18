number=int(input("Enter a number: "))
for i in range(1,number+1):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else :
    print(i)

#using functions 
number=int(input("Enter a number: "))
def fizzbuzz(i):
  if i%3==0 and i%5==0:
    return "FizzBuzz"
  elif i%3==0:
    return "Fizz"
  elif i%5==0:
    return "Buzz"
  else : 
    return i
for x in range(1,number+1):
  print(fizzbuzz(x))

  
