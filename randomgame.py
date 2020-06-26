import sys
from random import randint


first = int(sys.argv[1])
last = int(sys.argv[2])

while True:
	print(f'numbers are between  {first} and {last}')
	
	while True:
		try:
			num = int(input('Choose a number:'))
			if first <= num <= last:
				if num == randint(first,last):
					print('you are a genius!')
					break
				else:
					print('sorry, try again')
			break

		except ValueError:
			print('Please enter a number')
		
