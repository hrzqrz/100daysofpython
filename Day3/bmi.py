print('this program calculate BMI.')
height = float(input('enter your height in m: '))
weight = int(input('enter your weight in KG:'))
bmi = round(weight / height ** 2)
if bmi <= 18.5:
    print(f'your bmi is {bmi} and you are underweight.')
elif bmi <= 25 :
    print(f'your bmi is {bmi} and you are normal weight.')
elif bmi <= 30:
    print(f'your bmi is {bmi} and you are overweight.')
elif bmi < 35:
    print(f'your bmi is {bmi} and you are clinically obese.')
else:
    print('enter your weight and height.')
    
    
    