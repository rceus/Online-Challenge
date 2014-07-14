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
