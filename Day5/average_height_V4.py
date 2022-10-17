heights = input('Enter each student height: ').split()

len_of_heights = 0 

for height in heights:
    len_of_heights += 1
    
for n in range(0, len_of_heights):
    heights[n] = int(heights[n])
    
total_height = 0

for height in heights:
    total_height += height
    
average = round( total_height / len_of_heights )

print(f'There are {len_of_heights} students and the average height is : {average}')