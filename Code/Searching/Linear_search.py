def linear_search(x,s):
	for i in x:
		if x[i] == s:
			return i
	return -1


x = [1,2,4,5,6,19,10]
s = 10
print(linear_search(x,s))
