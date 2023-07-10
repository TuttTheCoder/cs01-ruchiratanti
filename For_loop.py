num = int(input("input number1: "))
if (num >= 0 ) and (num <= 1000):
    for count in range(1,num):
        num += count
    print("Output: ", num)
else:
    print("your number is less than 0 or greater than 1000")
print()

num2 = int(input("input number2: "))
if (num2 >= 0 ) and (num2 <= 1000):
    for count2 in range(1,11):
        print(f"{num2} x {count2} = {num2*count2}")
else:
    print("your number is less than 0 or greater than 1000")
print()

num3 = int(input("input number3: "))
ans=1
if (num3 >= 0 ) and (num3 <= 1000):
    for count3 in range(num3+1):
        if count3%2 != 0:
            ans += 1
            print(count3)

else:
    print("your number is less than 0 or greater than 1000")
print()

num4 = int(input("input number4: "))
if (num4 >= 0 ) and (num4 <= 1000):
    for count4 in range(num4+1):
        print(count4*"*")
else:
    print("your number is less than 0 or greater than 1000")
print()