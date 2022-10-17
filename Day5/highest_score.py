print('This code calculate the highest score in this list.')

scores = input('Enter the scores: ').split()

len_of_scores = len(scores)

for i in range(0, len_of_scores):
    scores[i] = int(scores[i])
    
highest_score = 0 

for score in scores:
    if score > highest_score:
        highest_score = score

print(f'The highest score is {highest_score}')