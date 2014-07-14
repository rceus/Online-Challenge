"""
	Four cases to consider:

	When looping again on the array: (Output)
	One: No zeroes in the array: Print the product divided by the interated element
	Two: Two or more zeroes: Print 0 for the whole array
	Three: One zero:
		Subcase 1: Print 0 if the current element is not a zero
		Subcase 2: Print the product if the current element is a zero
"""
def main():
	product = 1
	length = int(input())
	zeroes = 0
	arr = []

	for i in range(length):
		number = int(input())
		if number==0:
			zeroes +=1
		else:
			product *= number
		arr.append(number)

	if zeroes > 1:
		for i in range(len(arr)):
			print(0)
	elif zeroes == 0:
		for j in xrange(len(arr)):
			print(product//arr[j])
	else: #zeroes are 1
		for k in xrange(len(arr)):
			if arr[k] == 0:
				print(product)
			else:
				print(0)

if __name__ == '__main__':
	main()
