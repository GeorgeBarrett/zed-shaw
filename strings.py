types_of_cheese = 1000
x = f'there are {types_of_cheese} types of cheese'

binary = 'binary'
do_not = 'don\'t'
y = f'there are those who know {binary} and those who {do_not}'

print(f'I say {x}')
print(f'I also say {y}')

hilarious = False

joke_evaluation = 'Is living in a damp overly priced house funny? {}'

print(joke_evaluation.format(hilarious))