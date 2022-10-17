students_height = input('Input a list of students heights: ').split()
len_of_students_height = len(students_height)
for n in range(0, len_of_students_height):
    students_height[n] = int(students_height[n])
sum = 0 

for height in students_height:
    sum += height

average = round(sum / len_of_students_height)

print(f'There are a total of {len_of_students_height} studensts and the average height is {average}')
# print(students_height)