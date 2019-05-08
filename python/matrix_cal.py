# calculate matrix AX=Y

A = [[1, 1, 1, 0],
     [3, 4, 2, 1],
     [5, 8, 0, 9],
     [2, 3, 1, 1],
     [1, 0, 4, 5]]
X = [1, 1, 1, 1]

m = len(A)
n = len(A[0])
# the matrix is an m*n matrix

print("matrix A is:")
for a in range(0,m):
    print(*A[a])

print("m =",m,"and n =",n)

print("matrix X is:")                    # transpose the metrix
for b in range(0,n):
    print(X[b])

Y = []                                   # set Y as empty matrix

# Calculation:
for i in range(0,m):
    temp = 0
    for j in range(0,n):
        temp = temp + A[i][j] * X[j]     # y[i] = sum(a[i][j] + x[j])
    Y.append(temp)                       # add the Y items one by one


print("The result matrix Y is:")
for c in range(0,m):
    print(Y[c])
