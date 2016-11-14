grades = {'Gale': {'Homework 1': 88, 'Homework 2': 76}, 'Jordan': {'Homework 1': 92, 'Homework 2': 87},
          'Peyton': {'Homework 1': 84, 'Homework 2': 77}, 'River': {'Homework 1': 85, 'Homework 2': 91}}

#
# for student in grades:
#     print(student)
#
#
# print(grades["Gale"]["Homework 1"])
#
#
# for student in grades:
#     for grade in student:
#         print(grade)

test_var = [students for p, students in grades.items()]


x = 0
count = 0
for item in test_var:
    print(item)
    for value in item:
        print(item[value])
        count += 1
        x += item[value]
print(x)
print(count)
average = x / count
print(average)


lst = [(item, value) for item in test_var for value in item]
