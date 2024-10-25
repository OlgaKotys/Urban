grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Jonny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)

grades[0] = sum(grades[0])/len(grades[0])
grades[1] = sum(grades[1])/len(grades[1])
grades[2] = sum(grades[2])/len(grades[2])
grades[3] = sum(grades[3])/len(grades[3])
grades[4] = sum(grades[4])/len(grades[4])

n = 0
dict_ = {}
while n < len(students):
    dict_[students[n]] = grades[n]
    n += 1
print(dict_)