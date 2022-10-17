students_height = input('Input the students Height: ').split()
len_of_students_height = len(students_height)
for n in range(0, len_of_students_height):
    students_height[n] = int(students_height[n])
    
print(students_height)

total_height = sum(students_height)
print(total_height)
average_height = round(total_height / len_of_students_height)

print(f'There a {len_of_students_height} studensts and thier average height is: {average_height}')