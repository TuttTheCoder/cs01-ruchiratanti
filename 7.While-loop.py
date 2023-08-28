#1
print()
print('1) end = 0')
while True:
    one = int(input('input number '))
    print('output number',one)
    if one == 0:
        print('output number',one)
        break

#2 ts = twosum
print()
print('2) end must > 100')
two = int(input('input number '))
if two < 100:
    while True:
        print('output number',two)
        ts = int(input('sum with '))
        two += ts
        if two >= 100:
            print('final answer',two)
            break

#3 tc = threecount
print()
print('3) end = 0')
tc = 0
while True:
    tc += 1
    three = int(input('input number '))
    print('count:',tc)
    if three == 0:
        print('count:',tc)
        break

print()
print('4) end = 0')
four = int(input('input number '))
fourc = 0
while fourc < four:
    print('*', end='')
    fourc += 1
    if four == 0:
        break
    elif four <0:
        print('invalid number--->',four)
        break

#5
print()
print('5) end > 1000')
five = int(input('input number '))
if five == 0:
        print("Error: zero cannot multiple by two to 1000")
else:
    while True:
        print('output number',five)
        five *= 2
        if five > 1000:
            print('output number',five)
            break