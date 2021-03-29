string = 'Four score and seven years ago'
string_to_find = 'eight'
position = string.find(string_to_find)
if position != -1:
    print(f'The word {string_to_find} was found at index {position}')
else:
    print(f'The word {string_to_find} was not found, position is {position}.')
