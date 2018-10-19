T = int(input()) #No. of test cases
for i in range(T):
	N = int(input())
	arr = list(map(int, input().split()))
	PN = 1 + arr[0]
	day = 1
	QN = 0
	total = 0
	while(PN < N):
		if QN == 0:
			QN = PN
			total = sum(arr[:PN])
			PN += total
		else:
			total += sum(arr[QN:PN])
			QN = PN
			PN += total
		
		day += 1

	print(day)
