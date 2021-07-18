def binary_serach(x,s,first,last):
	while first <= last:
		mid = first + (last-first)//2
		if x[mid] == s:
			return x[mid]
			
		elif x[mid]>s:
			last = mid -1
		else:
			first = mid+1
	return -1

x = [1,2,3,4,5,6,7]
s = 20
first = 0
last = len(x) - 1


print(binary_serach(x,s,first,last))
