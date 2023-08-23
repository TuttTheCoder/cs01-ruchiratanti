#1
print()
print('1) end = 0')
one = int(input('input number '))
while one !=0:
    print('output number',one)
    one = int(input('input number '))
    if one == 0:
        print('output number',one)
        break

#2 ts = twosum
print()
print('2) end must > 100')
two = int(input('input number '))
while two <= 100:
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
three = int(input('input number '))
while three !=0:
    tc += 1
    print('count:',tc)
    three = int(input('input number '))
    if three == 0:
        print('count:',tc)
        break

#4 ไม่ได้มาวันที่สอน อะไรคือ print("ใช่ end",end=' ') ครับ
print()
print('4) end = 0')
four = int(input('input number '))
while four >0:
    
    print('output ',four*'*')
    four = int(input('input number '))
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
    while five !=0:
        print('output number',five)
        five *= 2
        if five > 1000:
            print('output number',five)
            break