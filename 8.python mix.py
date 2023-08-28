print('1.end = -1')
while True:
    one = int(input('input: '))
    if one == -1: break
print('stopped')
print()

print('2.end in 10 input')
two = 0
for i in range (10):
    t = 0 ; t = int(input('input: '))
    if t < 0:
        continue
    else:
        two = two + t
print(two)
print()

print('3.end in 3 input')
a = int(input('input: '))
b = int(input('input: '))
c = int(input('input: '))
if a > b and a > c:
    print(a)
else: pass
if b > c and b > a:
    print(b)
else: pass
if c > a and c > b:
    print(c)
else: pass
print()

print('4.add')
def add(f1,f2):
    sum = f1+f2
    print('output:',sum)
add(3,4)