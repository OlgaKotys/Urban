from fake_math import divide as fake_d
from true_math import divide as true_d

result1 = fake_d(99, 3)
result2 = fake_d(5, 0)
result3 = true_d(77, 7)
result4 = true_d(30, 0)

print(result1)
print(result2)
print(result3)
print(result4)