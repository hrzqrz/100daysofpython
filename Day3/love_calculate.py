from itertools import count


print('Welcome to the love calculator!')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

name1 = name1.lower()
name2 = name2.lower()
both_names = name1 + name2
# print(both_names)
true_counter = 0
t_count = both_names.count('t')
# print(f'{t_count}')
r_count = both_names.count('r')
u_count = both_names.count('u')
e_count = both_names.count('e')
# print(f'{e_count}')
true_counter = t_count + r_count + u_count + e_count

l_count = both_names.count('l')
# print(f'{t_count}')
o_count = both_names.count('o')
v_count = both_names.count('v')
e_count = both_names.count('e')

love_count = l_count + o_count + v_count + e_count

love_score = int(str(true_counter) + str(love_count))


# print(love_score)

if love_score < 10 or love_score > 90:
    print(f'Your love score is {love_score}, you go togethe like ww2')
elif love_score >= 40 and love_score <=50:
    print(f'your score is {love_score}, you are alright together.')
else:
    print(f'your score is {love_score}')

