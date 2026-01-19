def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)
def generate_fizzbuzz(num):
    result = []
    for i in range(1, num + 1):
        result.append(fizzbuzz(i))
    return result
n = int(input("Enter a number: "))
print(generate_fizzbuzz(n))

