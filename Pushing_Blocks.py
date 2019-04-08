print("Enter M, P, F: \n")
stack = list(map(int, input().split()))
M = stack[0]
P = stack[1]
F = stack[2]

rowList = []

for i in range(M):
	row = list(map(int, input().split()))
	rowList.append(row)

for i in range(M):
	print(rowList[i])

f_input = list(map(int, input().split()))
k = 0

for j in range(P-1, -1, -1):
	for i in range(M-1, -1, -1):
		if(rowList[i][j] == 0 and k < F):
			rowList[i][j] = f_input[k]
			k += 1

for i in range(M):
	print(rowList[i])
