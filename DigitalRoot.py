
"""DIGITAL ROOT AND ADDITIVE PERSISTANCE: 
Digital root is the single digit obtained after recursive sum of all the digits in a number.
This simple python function finds the digital root of a number"""

def DigitalRoot(number):
	addper = 0
	while number >=10:
		number = sum(int(digit)for digit in str(number))
		addper +=1
	#I highly recommend using return instead of print, but for testing purposes I used print
	print(addper)
	print(number)
DigitalRoot(895)

"""ALTERNATIVE SOLUTION:"""
userNumber= 674
rootResult = userNumber % 9
if rootResult == 0:
	print(9)
else:
	print(rootResult)
