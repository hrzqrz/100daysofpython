row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

rows_map = [row1, row2, row3]

# print(f'{row1}\n{row2}\n{row3}')
# print(rows_map)

position = input('Where do you wnant to put treasure? ')
row_map = int(position[0])
column_map = int(position[1])
if row_map > 3 or column_map > 3:
    print('Enter a number under 3.')
else:
    rows_map[row_map - 1 ][column_map - 1] = 'X'
    print(f'{row1}\n{row2}\n{row3}')