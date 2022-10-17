print('This program calculate the average height of your students: ')
student_heights = [180, 200, 156, 120, 193, 140, 175]

len_of_student_heights = len(student_heights)

sum = 0 

for height in student_heights:
    sum += height

average = round(sum / len_of_student_heights)

print(f'There are a total of {len_of_student_heights} studensts and the average height is {average}') 