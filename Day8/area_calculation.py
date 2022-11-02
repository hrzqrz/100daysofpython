import math
print('Hi, this program calculate the area and how many cans do you need to paint the wall.')
width = int(input('width: '))
heighet = int(input('height: '))
coverage = 5
def area_calc(width, height, cover):
    area =  (width * height) / 10
    number_of_cans = math.ceil(area / cover)
    print(f'You need {number_of_cans} cans for this painting.')
    
area_calc(width=width, height=heighet, cover=coverage)
