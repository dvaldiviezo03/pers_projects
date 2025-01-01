n = int(input("enter a num: ")) 
if n%3 == 0 and n%5 == 0: # need the "==0" this checks that it IS divisible by 3 and 5
    print("FizzBuzz")
elif n%3 == 0:
    print("Fizz")
elif n%5 == 0:
    print("Buzz")
else:
    print(n)