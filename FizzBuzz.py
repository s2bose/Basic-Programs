#Basic FizzBuzz program in Python3

print("Welcome to the FizzBuzz program")

num1 = int(input("Please enter the initial number: "))
num2 = int(input("Please enter the ending number: "))

for x in range(num1, num2+1):
  if (x%15==0):
    print("FizzBuzz")
  elif (x%3==0):
    print("Fizz")
  elif (x%5==0):
    print("Buzz")
  else:
    print(x)
