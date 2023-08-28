wp = float(input('กรุณาใส่คะแนนเก็บของคุณ: '))
mp = float(input('กรุณาใส่คะแนนสอบกลางภาคของคุณ: '))
fp = float(input('กรุณาใส่คะแนนสอบปลายภาคของคุณ: '))
score = wp+mp+fp
if score > 100:
    grade = 'idiot'
if score >= 80:
    grade = 'A'
elif score >= 75:
    grade = 'B+'
elif score >= 70:
    grade = 'B'
elif score >= 65:
    grade = 'C+'
elif score >= 60:
    grade = 'C'
elif score >= 55:
    grade = 'D+'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'
print('เกรดของคุณคือ:',grade)