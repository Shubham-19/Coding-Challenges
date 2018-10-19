T = int(input())

for i in range(T):
	num = list(map(int, input().split()))
	arr = sorted(list(map(int, input().split())), reverse = True)
	ind = num[0] - arr[::-1].index(arr[num[1]-1])
	print(ind)
