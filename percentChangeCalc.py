#Percent Change Calculator
print('Welcome to the percent change calc')
original= float(input('First Value: '))
change= float(input('Second Value: '))

#------------#

#percent calc
def percentChange(original,change):
	percent = ((change-original)/original)
	formatPercent= str(abs(percent) *100)
	print(f'{formatPercent}%')


#------------#
if original == change:
	print('No % change')
elif original < change:
	print('Percent INCREASE')
	percentChange(original,change)
elif original > change:
	print('Percent DECREASE')
	percentChange(original,change)
else:
	print('Error')