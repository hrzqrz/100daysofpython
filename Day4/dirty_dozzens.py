dirty_dozen = ['strawberries', 'spinach', 'kale', 'nectarines', 'apple', 'grapes', 'peaches', 
               'cherries', 'pears', 'tomatos', 'celery', 'potatoes']
fruits = ['strawberries', 'nectarines', 'apple', 'grapes', 'peaches', 'cherries', 'pears']
vegetales = ['spinach', 'kale', 'tomatos', 'celery', 'potatoes']
combine_fruits_vegetables = [fruits, vegetales]
print(combine_fruits_vegetables)
dirty_dozen_title = []
for fruit in dirty_dozen:
    dirty_dozen_title.append(fruit.title())
print(dirty_dozen_title) 