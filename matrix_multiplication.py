#using nested list comprehension

X = [[2, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

Y = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
     
result = [[sum(a*b for a,b in zip(xrow,ycol)) for ycol in zip(*Y)] for xrow in X]
print(result)

#for loop:

trial=[]
for xrow in X:
    ans=[]
    for ycol in zip(*Y):
        ans1=sum(a*b for a,b in zip(xrow,ycol))
        ans.append(ans1)
    trial.append(ans)
print(trial)

#for loop alternative

trial2 = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           trial2[i][j] += X[i][k] * Y[k][j]
print(trial2)