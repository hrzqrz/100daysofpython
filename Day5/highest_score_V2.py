scores = input('Enter the socres here: ').split()

len_of_scores = len(scores)

for i in range(0, len_of_scores):
    scores[i] = int(scores[i])
     
max_score = max(scores)

print(f'The highest score in the class is: {max_score}')