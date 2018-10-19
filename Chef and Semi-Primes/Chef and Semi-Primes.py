def checkSemiprime(n): 
    cnt = 0
  	
    for i in range(2, int(n**.5) + 1): #complexity is O(logn)
        while n % i == 0: 
            n /= i 
            cnt += 1
        if cnt >= 2:  
            break
    if(n >= 1): 
        cnt += 1
  
    return cnt == 2

t = int(input())
arr = []
arr_1 = []

for i in range(0, t):
	num = int(input())
	arr.append(num)
	
a = max(arr)
for i in range(2, a):
	if(checkSemiprime(i)):
		arr_1.append(i)

for entry in arr:
	for value in arr_1:
		pair_found = False
		a = entry - value
		if a in arr_1:
			pair_found = True
			break
	
	if(pair_found):
		print('YES')
	else:
		print('NO')
		
