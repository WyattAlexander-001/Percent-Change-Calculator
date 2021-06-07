#Percent Change Calculator
print('''

Percent Change Calculator
Basis of formula:

((V2-V1)/|V1|) * 100

V2 = new value
V1 = original value

'''
)
def main():
	
	print('Welcome to the percent change calc')
	original= float(input('First Value: '))
	change= float(input('Second Value: '))
	
	#------------#
	
	#percent calc
	def percentChange(original,change):
		percent = ((change-original)/abs(original)*100)
		percent = abs(percent)
		percent = round(percent,3)
		print(f'{percent}%')
	
	
	#------------#
	if original == change:
		print('No % change')
	elif original < change:
		print('Percent INCREASE of:')
		percentChange(original,change)
	elif original > change:
		print('Percent DECREASE of:')
		percentChange(original,change)
	else:
		print('Error')

	x = input('Try again? Type Yes or No:\n\n').lower()
	if x == 'yes':
	   main()
	else:
	 print('Error')
  

main()
	